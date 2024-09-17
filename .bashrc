#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

(cat ~/.cache/wal/sequences &)

alias ls='ls --color=auto'
PS1="\[\033[01;32m\]\u\[\033[00m\]@\[\033[01;34m\]\h\[\033[00m\] \[\033[01;36m\]\W\[\033[00m\] $ "

export EDITOR=nvim
export TT_USERNAME=????????
export TT_PASSWORD="????????"
export TT_ACCOUNT=????????
export PATH=$PATH:/home/graeme/.local/bin

set -o vi

alias l='ls --color=auto'
alias la='ls -a --color=auto'
alias ll='ls -lh --color=auto'
alias c='clear'
alias lf='ranger'

#eval "$(_TT_COMPLETE=bash_source tt)"
alias vim="nvim"
