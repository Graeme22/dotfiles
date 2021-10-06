set tabstop=4
set showmatch
set smarttab
set shiftwidth=4
filetype off
filetype plugin indent on
syntax on
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview 
