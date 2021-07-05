#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

(cat ~/.cache/wal/sequences &)

alias ls='ls --color=auto'
PS1="[\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]:\[\033[01;36m\]\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)\[\033[00m\]]$ "

export EDITOR=vim
export TW_USER=graeme22
export PATH=$PATH:/home/graeme/.local/bin

alias l='ls'
alias la='ls -a'
alias ll='ls -lh'
alias c='clear'
alias lf='ranger'
