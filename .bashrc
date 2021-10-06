#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

(cat ~/.cache/wal/sequences &)

alias ls='ls --color=auto'
PS1="\[\033[01;32m\]\u\[\033[00m\]@\[\033[01;34m\]\h\[\033[00m\] \[\033[01;36m\]\W\[\033[00m\] $ "

export EDITOR=vim
export TW_USER=????????
export TW_ACC=????????
export PATH=$PATH:/home/graeme/.local/bin

alias l='ls'
alias la='ls -a'
alias ll='ls -lh'
alias c='clear'
alias lf='ranger'
