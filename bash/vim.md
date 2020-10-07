vim
搜索选中的部分
https://superuser.com/questions/41378/how-to-search-for-selected-text-in-vim
select(visual)
y
/
ctrl +r + "
enter

编码问题
# 查看编码
set fileencoding
# 转换编码
set fileencoding=utf8

```
let mapleader=','
# 去除搜索的标志， normal下,/即可
noremap <silent><leader>/ :nohls<CR>
# 跨panel复制粘贴
vmap <leader>y :w! ~/.vbuf<cr>
nmap <leader>p :r ~/.vbuf<cr>
```