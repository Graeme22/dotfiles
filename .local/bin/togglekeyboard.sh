#!/bin/bash

if xkblayout-state print "%s" | grep -q 'us'; then
	setxkbmap es
elif xkblayout-state print "%s" | grep -q 'es'; then
	setxkbmap gr
else
	setxkbmap us
fi
