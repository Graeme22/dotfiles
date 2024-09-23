#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

(cat ~/.cache/wal/sequences &)

alias ls='ls --color=auto'
PS1="\[\033[01;32m\]\u\[\033[00m\]@\[\033[01;34m\]\h\[\033[00m\] \[\033[01;36m\]\W\[\033[00m\] $ "

export EDITOR=vim
export TT_USERNAME=graeme22
export TT_PASSWORD="CM,TXk):|S2sB[~;<]u^9L/g^"
export TT_ACCOUNT=5WU50895
export PATH=$PATH:/home/graeme/.local/bin
export PATH=$PATH:/home/graeme/.modular/bin

set -o vi

alias l='ls --color=auto'
alias la='ls -a --color=auto'
alias ll='ls -lh --color=auto'
alias c='clear'
alias lf='ranger'

alias vim="nvim"
export LD_LIBRARY_PATH=/home/graeme/.local/lib/arch-mojo:$LD_LIBRARY_PATH

. "$HOME/.cargo/env"
