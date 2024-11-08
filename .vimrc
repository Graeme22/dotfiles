set tabstop=4
set showmatch
set smarttab
set shiftwidth=4
filetype off
filetype plugin indent on
syntax on
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview 
let &t_SI = "\e[5 q"
let &t_SR = "\e[3 q"
let &t_EI = "\e[2 q"
