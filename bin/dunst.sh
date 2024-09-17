#!/bin/sh

[ -f "$HOME/.cache/wal/colors.sh" ] && . "$HOME/.cache/wal/colors.sh"

pidof dunst && killall dunst

dunst -lf  "$foreground" \
	  -lb  "$color1" \
	  -nf  "$foreground" \
	  -nb  "$color1" \
	  -cf  "$foreground" \
	  -cb  "$color1" > /dev/null 2>&1 &
