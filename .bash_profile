#
# ~/.bash_profile
#

export GPG_TTY=$(tty)
export EDITOR=vim
export LIBSEAT_BACKEND=logind
export LC_ALL=en_US.utf8
export GRIM_DEFAULT_DIR="/home/graeme/Pictures"
export QT_QPA_PLATFORM=wayland
export QT_QPA_PLATFORMTHEME=qt5ct
export ECORE_EVAS_ENGINE=wayland_egl
export ELM_ENGINE=wayland_egl
export ELM_DISPLAY=wl
export ELM_ACCEL=opengl
export _JAVA_AWT_WM_NONREPARENTING=1

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ "$(tty)" = "/dev/tty1" ]; then
	[[ $(fgconsole 2>/dev/null) == 1 ]] && exec qtile start -b wayland
fi
