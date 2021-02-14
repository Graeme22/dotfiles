#!/bin/bash

if xkblayout-state print "%s" | grep -q 'us'; then
	setxkbmap es
else
	setxkbmap us
fi
