#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export GEM_HOME="$(ruby -e 'puts Gem.user_dir')"
export PATH="$PATH:$GEM_HOME/bin"

(cat ~/.cache/wal/sequences &)

alias ls='ls --color=auto'
PS1="[\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]:\[\033[01;36m\]\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)\[\033[00m\]]$ "

alias l='ls'
alias la='ls -a'
alias ll='ls -lh'
alias c='clear'
alias vi='vim'
alias mail='TERM=screen-256color neomutt'

alias jam='spt play --playlist --name'
alias skip='spt playback -n'
alias toggle='spt playback --toggle'

alias code='codium'
alias lf='ranger'

# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"
