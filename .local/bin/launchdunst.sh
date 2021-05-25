#!/bin/sh

[ -f "$HOME/.cache/wal/colors.sh" ] && . "$HOME/.cache/wal/colors.sh"

pidof dunst && killall dunst

dunst -lf  "$color1" \
      -lb  "$color6" \
      -nf  "$color1" \
      -nb  "$color6" \
      -cf  "$color1" \
      -cb  "$color6" > /dev/null 2>&1 &

