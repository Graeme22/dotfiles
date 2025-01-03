#!/bin/sh
/usr/bin/pipewire 2>&1 &
/usr/bin/pipewire-pulse 2>&1 &
/usr/bin/wireplumber 2>&1 &
