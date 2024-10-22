#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1="\[\033[01;32m\]\u\[\033[00m\]@\[\033[01;34m\]\h\[\033[00m\] \[\033[01;36m\]\W\[\033[00m\] $ "

export EDITOR=vim
set -a; source ~/.env; set +a
export EDITOR=nvim
export PATH=$PATH:/home/graeme/.local/bin
export PATH=$PATH:/home/graeme/.modular/bin

set -o vi

alias l='ls --color=auto'
alias la='ls -a --color=auto'
alias ll='ls -lh --color=auto'
alias c='clear'
alias lf='ranger'
alias vim="nvim"

. "$HOME/.cargo/env"
