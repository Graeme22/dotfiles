#!/bin/sh
pidof dunst && killall dunst
dunst > /dev/null 2>&1 &
