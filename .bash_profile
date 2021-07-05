#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

[[ $(fgconsole 2>/dev/null) == 1 ]] && exec startx -- vt1

export GPG_TTY=$(tty)
export EDITOR=vim
