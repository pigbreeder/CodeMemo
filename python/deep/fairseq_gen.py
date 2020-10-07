fairseq中transformer在推理的时候和训练时候区别很大，主要以下内容
1 encoder 一样
2 decoder 用的不一样，主要是每次decoder都是一个token送进去，然后计算用cache内容
3 beam时候的topk

def _generate(self, encoder_input):
        src_tokens = encoder_input['src_tokens'] # shape=batch,length
        # length of the source text being the character length except EndOfSentence and pad
        # 两个not equal 并起来然后sum按照第一个维度加得到[bsz] 长度
        src_lengths = (src_tokens.ne(self.eos) & src_tokens.ne(self.pad)).long().sum(dim=1)
        # bsz: total number of sentences in beam
        bsz, srclen = src_tokens.size()

        # the max beam size is the dictionary size - 1, since we never select pad
        beam_size = min(self.beam_size, self.vocab_size - 1)

        incremental_states = {}
        self.model.eval()
        if isinstance(self.model.decoder, FairseqIncrementalDecoder):
            incremental_states[self.model] = {}
        else:
            incremental_states[self.model] = None

        # compute the encoder output for each beam
        # 这里没变直接算一次即可
        encoder_out = self.model.encoder(**encoder_input)
        # placeholder of indices for bsz * beam_size to hold tokens and accumulative scores
        new_order = torch.arange(bsz).view(-1, 1).repeat(1, beam_size).view(-1)
        new_order = new_order.to(src_tokens.device).long()
        encoder_out = self.model.encoder.reorder_encoder_out(encoder_out, new_order)

        # initialize buffers
        scores = src_tokens.data.new(bsz * beam_size, self.maxlen + 1).float().fill_(0) # +1 for eos; pad is never choosed for scoring
        tokens = src_tokens.data.new(bsz * beam_size, self.maxlen + 2).fill_(self.pad) # +2 for eos and pad
        # 初始位置设置为eos，bos和eos统一了
        tokens[:, 0] = self.eos

        # list of completed sentences
        finalized = [[] for i in range(bsz)] # contains lists of dictionaries of infomation about the hypothesis being finalized at each step
        finished = [False for i in range(bsz)] # a boolean array indicating if the sentence at the index is finished or not
        num_remaining_sent = bsz # number of sentences remaining

        # number of candidate hypos per step
        # 避免一半都是eos情况，所以设置为2倍的beam_size
        cand_size = 2 * beam_size  # 2 x beam size in case half are EOS

        # offset arrays for converting between different indexing schemes
        # 这个是为了后面选择非eos增加偏移量设置的
        cand_offsets = torch.arange(0, cand_size).type_as(tokens)

        def finalize_hypos(step, bbsz_idx, eos_scores):
            """Finalize hypothesis, store finalized information in `finalized`, and change `finished` accordingly.
            Returns number of sentences being finalized.
            Args:
                bbsz_idx (Tensor):
            """
            assert bbsz_idx.numel() == eos_scores.numel()

            # clone relevant token and attention tensors
            tokens_clone = tokens.index_select(0, bbsz_idx)[:, 1:step + 2] # skip the first index, which is EOS
            tokens_clone[:, step] = self.eos

            # compute scores per token position
            pos_scores = scores.index_select(0, bbsz_idx)[:, :step+1]
            pos_scores[:, step] = eos_scores
            # convert from cumulative to per-position scores
            pos_scores[:, 1:] = pos_scores[:, 1:] - pos_scores[:, :-1]

            # normalize sentence-level scores
            if self.normalize_scores:
                eos_scores /= (step + 1) ** self.len_penalty

            sents_seen = set()
            for i, (idx, score) in enumerate(zip(bbsz_idx.tolist(), eos_scores.tolist())):
                sent = idx // beam_size
                sents_seen.add(sent)

                if len(finalized[sent]) < beam_size:
                    finalized[sent].append({
                        'tokens': tokens_clone[i],
                        'score': score,
                        'attention': None, # src_len x tgt_len
                        'alignment': None,
                        'positional_scores': pos_scores[i],
                    })

            newly_finished = 0
            for sent in sents_seen:
                # check termination conditions for this sentence
                if not finished[sent] and len(finalized[sent]) == beam_size:
                    finished[sent] = True
                    newly_finished += 1
            return newly_finished

        reorder_state = None
        for step in range(self.maxlen + 1):  # one extra step for EOS marker
            # reorder decoder internal states based on the prev choice of beams
            if reorder_state is not None:
                if isinstance(self.model.decoder, FairseqIncrementalDecoder):
                    self.model.decoder.reorder_incremental_state(incremental_states[self.model], reorder_state)
                encoder_out = self.model.encoder.reorder_encoder_out(encoder_out, reorder_state)

            # 内部的_decode() 扔进去也是单个字符，lprobs是(bsz * beam_size, vocab_prob)
            lprobs = self._decode(tokens[:, :step + 1], encoder_out, incremental_states)

            lprobs[:, self.pad] = -math.inf  # never select pad
            lprobs[:, self.unk] -= self.unk_penalty  # apply unk penalty

            scores = scores.type_as(lprobs)
            eos_bbsz_idx = tokens.new() # indices of hypothesis ending with eos (finished sentences)
            eos_scores = scores.new() # scores of hypothesis ending with eos (finished sentences)
            if step < self.maxlen:
                self.search.set_src_lengths(src_lengths)
                # 返回的shape=(bsz,beam_size*2) scores是分数，indices是每个候选集合当前步对应的vocab_idx，beams是说这个是归属于哪个beam
                cand_scores, cand_indices, cand_beams = self.search.step(
                    step,
                    lprobs.view(bsz, -1, self.vocab_size),
                    scores.view(bsz, beam_size, -1)[:, :, :step],
                )
            else:
                # make probs contain cumulative scores for each hypothesis
                lprobs.add_(scores[:, step - 1].unsqueeze(-1))

                # finalize all active hypotheses once we hit maxlen
                # pick the hypothesis with the highest prob of EOS right now
                torch.sort(
                    lprobs[:, self.eos],
                    descending=True,
                    out=(eos_scores, eos_bbsz_idx),
                )
                num_remaining_sent -= finalize_hypos(step, eos_bbsz_idx, eos_scores)
                assert num_remaining_sent == 0
                break

            # cand_bbsz_idx contains beam indices for the top candidate
            # hypotheses, with a range of values: [0, bsz*beam_size),
            # and dimensions: [bsz, cand_size]
            # 把原先对应于beam的位置对应到bsz*beam这个位置上，eg：cand_beams=1，说明是第一个beam，但是对应第几个bsz中的beam=1
            cand_bbsz_idx = cand_beams.add((torch.arange(0, bsz) * beam_size).unsqueeze(1).type_as(tokens))

            # finalize hypotheses that end in eos
            eos_mask = cand_indices.eq(self.eos)

            # only consider eos when it's among the top beam_size indices
            # masked_select选出来的是1-D Tensor，直接把cand_bbsz中eos选出来，上面用indices是只有vocab_idx才能判断eos
            eos_bbsz_idx = torch.masked_select(
                cand_bbsz_idx[:, :beam_size],
                mask=eos_mask[:, :beam_size],
            )
            if eos_bbsz_idx.numel() > 0:
                torch.masked_select(
                    cand_scores[:, :beam_size],
                    mask=eos_mask[:, :beam_size],
                    out=eos_scores,
                )
                num_remaining_sent -= finalize_hypos(step, eos_bbsz_idx, eos_scores)

            if num_remaining_sent == 0:
                break

            # set active_mask so that values > cand_size indicate eos hypos
            # and values < cand_size indicate candidate active hypos.
            # After, the min values per row are the top candidate active hypos
            
            # 加法表明每行中添加偏移量（因为总的个数是cand_size所以offset为cand_offset)
            # 这样取最小就能得到对应的最大概率的vocab_idx，因为上一个topk得到结果越靠前prob越大
            # 这一波操作mask来mask去，active_mask就是去掉eos对应的score来计算。
            
            active_mask = torch.add(
                eos_mask.type_as(cand_offsets) * cand_size, #  第一个乘法表明大于cand_size的表示eos结束的示例
                cand_offsets[:eos_mask.size(1)],
            )

            # get the top beam_size active hypotheses, which are just the hypos
            # with the smallest values in active_mask
            # 第一波topk是2*beam，因为可能有eos情况，第二波topk就是去除掉eos同时把之前idx越小则对应越靠前，越应该选择。
            _, active_hypos = torch.topk(
                active_mask, k=beam_size, dim=1, largest=False,
            )

            # 得到最终的beam结果
            active_bbsz_idx = torch.gather(
                cand_bbsz_idx, dim=1, index=active_hypos,
            )
            # 对应的分数
            active_scores = torch.gather(
                cand_scores, dim=1, index=active_hypos,
            )

            # index_select要用1-D tensor
            active_bbsz_idx = active_bbsz_idx.view(-1)
            active_scores = active_scores.view(-1)


            # 下面的score和token都是先index再gather
            # tokens第一个维度是bsz*beam，index_select是选择出score高的bbsz这个维度对应的几个
            # gather是把数值对应起来放回去

            # copy tokens and scores for active hypotheses
            tokens[:, :step + 1] = torch.index_select(
                tokens[:, :step + 1], dim=0, index=active_bbsz_idx,
            )
            tokens.view(bsz, beam_size, -1)[:, :, step + 1] = torch.gather(
                cand_indices, dim=1, index=active_hypos,
            )

            scores[:, :step] = torch.index_select(
                scores[:, :step], dim=0, index=active_bbsz_idx,
            )
            scores.view(bsz, beam_size, -1)[:, :, step] = torch.gather(
                cand_scores, dim=1, index=active_hypos,
            )

            # reorder incremental state in decoder
            reorder_state = active_bbsz_idx

        # sort by score descending
        for sent in range(len(finalized)):
            finalized[sent] = sorted(finalized[sent], key=lambda r: r['score'], reverse=True)

        return finalized

    def _decode(self, tokens, encoder_out, incremental_states):
        with torch.no_grad():
            if incremental_states[self.model] is not None:
                decoder_out = list(self.model.decoder(tokens, encoder_out, incremental_state=incremental_states[self.model]))
            else:
                decoder_out = list(self.model.decoder(tokens, encoder_out))
            decoder_out[0] = decoder_out[0][:, -1, :]
        probs = self.model.get_normalized_probs(decoder_out, log_probs=True)
        return probs