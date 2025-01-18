#
# ~/.bash_profile
#

export GPG_TTY=$(tty)
export EDITOR=nvim
#export LC_ALL=en_US.utf8
#export GRIM_DEFAULT_DIR="/home/graeme/Pictures"
#export QT_QPA_PLATFORMTHEME=qt5ct
#export QT_QPA_PLATFORM=wayland
#export ECORE_EVAS_ENGINE=wayland_egl
#export ELM_ENGINE=wayland_egl
#export ELM_DISPLAY=wl
#export ELM_ACCEL=opengl
export _JAVA_AWT_WM_NONREPARENTING=1
export XDG_CURRENT_DESKTOP=qtile

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ "$(tty)" = "/dev/tty1" ]; then
	exec startx
fi
