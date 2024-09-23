dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=qtile

# Stop any services that are running, so that they receive the new env var when they restart.
systemctl --user stop pipewire wireplumber xdg-desktop-portal xdg-desktop-portal-wlr
systemctl --user start wireplumber xdg-desktop-portal
