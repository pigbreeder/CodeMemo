#!/bin/bash

#sbatch eval-one.slurm -p translate_youdao_j2_c -d /mfs_gpu/exec/xsy/train_data/gendata_0516_jp2cn -m /mfs_gpu/exec/xsy/train_model/jp2cn_model_20190530_deep_new_hparams/model.ckpt-5000 -H translate_youdao_j2c_deep_new_hparams -i /mfs_gpu/exec/xsy/test_data/jp/j2c/meiriyiju_tst.sub  -o /tmp/ -S jp -T cn -P test_ME

# eval j2c new_hparams
var=j2c_new_hp
sed "4s/log.eval.batch.*/log.eval.batch.$var/g" eval-batch.slurm >eval-batch.${var}.slurm
sbatch eval-batch.${var}.slurm -p translate_youdao_j2_c -d /mfs_gpu/exec/xsy/train_data/gendata_0516_jp2cn -m /mfs_gpu/exec/xsy/train_model/jp2cn_model_20190530_deep_new_hparams/ -H translate_youdao_j2c_deep_new_hparams -i /mfs_gpu/exec/xsy/test_data/jp/j2c/meiriyiju_tst.sub  -o /mfs_gpu/exec/xsy/eval_out/ -s 80000 -t 90000 -S jp -T cn -P eval_j2c_new_hp


# eval c2j new_hparams
var=c2j_new_hp
sed "4s/log.eval.batch.*/log.eval.batch.$var/g" eval-batch.slurm >eval-batch.${var}.slurm
sbatch eval-batch.${var}.slurm -p translate_youdao_c2_j -d /mfs_gpu/exec/xsy/train_data/gendata_0516_cn2jp -m /mfs_gpu/exec/xsy/train_model/cn2jp_model_20190530_deep_new_hparams/ -H translate_youdao_c2j_deep_new_hparams -i /mfs_gpu/exec/xsy/test_data/jp/c2j/meiriyiju_tst.sub  -o /mfs_gpu/exec/xsy/eval_out/ -s 80000 -t 90000 -S cn -T jp -P eval_c2j_new_hp


# eval j2c
var=j2c_old
sed "4s/log.eval.batch.*/log.eval.batch.$var/g" eval-batch.slurm >eval-batch.${var}.slurm
sbatch eval-batch.${var}.slurm -p translate_youdao_j2_c -d /mfs_gpu/exec/xsy/train_data/gendata_0516_jp2cn -m /mfs_gpu/exec/xsy/train_model/jp2cn_model_20190530_deep_old_hparams/ -H translate_youdao_j2c_deep_hparams -i /mfs_gpu/exec/xsy/test_data/jp/j2c/meiriyiju_tst.sub  -o /mfs_gpu/exec/xsy/eval_out/ -s 80000 -t 90000 -S jp -T cn -P eval_j2c_hp


# eval c2j
var=c2j_old
sed "4s/log.eval.batch.*/log.eval.batch.$var/g" eval-batch.slurm >eval-batch.${var}.slurm
sbatch eval-batch.${var}.slurm -p translate_youdao_c2_j -d /mfs_gpu/exec/xsy/train_data/gendata_0516_cn2jp -m /mfs_gpu/exec/xsy/train_model/cn2jp_model_20190530_deep_old_hparams/ -H translate_youdao_c2j_deep_hparams -i /mfs_gpu/exec/xsy/test_data/jp/c2j/meiriyiju_tst.sub  -o /mfs_gpu/exec/xsy/eval_out/ -s 80000 -t 90000 -S cn -T jp -P eval_c2j_hp
