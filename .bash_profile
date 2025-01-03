#
# ~/.bash_profile
#

export GPG_TTY=$(tty)
export EDITOR=nvim
export GRIM_DEFAULT_DIR="/home/graeme/Pictures"
export _JAVA_AWT_WM_NONREPARENTING=1
export XDG_CURRENT_DESKTOP=qtile

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ "$(tty)" = "/dev/tty1" ]; then
	/home/graeme/.local/bin/pipewire.sh > /dev/null 2>&1
	[[ $(fgconsole 2>/dev/null) == 1 ]] && exec dbus-run-session qtile start -b wayland
fi
