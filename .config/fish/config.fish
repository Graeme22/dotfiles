if status is-interactive
    # Commands to run in interactive sessions can go here
    fish_vi_key_bindings
    set fish_cursor_default block blink
    set fish_cursor_insert line blink
    set fish_vi_force_cursor
    bind -M insert \cy accept-autosuggestion
    bind -M default \cy accept-autosuggestion
end
