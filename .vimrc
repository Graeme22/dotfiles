set tabstop=4
set showmatch
set smarttab
set shiftwidth=4
filetype off
filetype plugin indent on
syntax on
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview 

set nocompatible

call plug#begin()
Plug 'sheerun/vim-polyglot'
call plug#end()

colorscheme wal
