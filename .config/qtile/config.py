import os
import random
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile import hook
from libqtile import qtile

from bluetooth import Bluetooth

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.local/bin/launchdunst.sh')
    subprocess.call([home])

wallpaper_path = '/home/graeme/.config/qtile/wallpapers'

colors = [
    '#131a17',
    '#699aaa',
    '#6fa1cf',
    '#7bc1d2',
    '#929fa8',
    '#c5c2b1',
    '#92b2d3',
    '#cadeea',
    '#ffffff',
]

mod = 'mod4'

keys = [
    # Switch window focus to other pane(s) of stack
    Key([mod], 'space', lazy.layout.next(), desc='Switch window focus to other pane(s) of stack'),

    # quick launch
    Key([mod], 'Return', lazy.spawn('alacritty'), desc='Launch terminal'),
    Key([mod], 'b', lazy.spawn('firefox')),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),

    Key([mod, 'control'], 'r', lazy.restart(), desc='Restart qtile'),

	# rofi launcher
    Key([mod], 'r', lazy.spawn('bash /home/graeme/.config/rofi/launchers/misc/launcher.sh')),

    # Volume control
	Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -D pulse sset Master 5%+ unmute')),
	Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -D pulse sset Master 5%- unmute')),
	Key([], 'XF86AudioMute', lazy.spawn('amixer -q set Master toggle')),

	# Brightness
	Key([], 'XF86MonBrightnessUp', lazy.spawn('xbacklight -inc 10')),
	Key([], 'XF86MonBrightnessDown', lazy.spawn('xbacklight -dec 10')),

	# lock screen / power off / reboot
	Key([mod], 'l', lazy.spawn('betterlockscreen --lock blur')),
    Key([mod, 'control'], 'q', lazy.shutdown()),

    # screenshot
    Key([mod], 'x', lazy.spawn('scrot \'%Y-%m-%d-%T_$wx$h_scrot.png\' -e \'mv $f ~/Pictures\'')),
]

groups = [Group(i) for i in 'asdf']

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc='Switch to group {}'.format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc='Switch to & move focused window to group {}'.format(i.name)),
    ])

layout_cfg = {
	'border_width': 3,
	'border_focus': colors[1],
	'margin': 8,
}

layouts = [
    layout.Max(**layout_cfg),
    layout.MonadTall(**layout_cfg),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
	foreground=colors[-1],
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(background=colors[6]),
                widget.Spacer(length=5, background=colors[6]),
				widget.TextBox(text='◣', background=colors[1], foreground=colors[6], fontsize=32, width=27, padding=-5),
                widget.GroupBox(background=colors[1], this_current_screen_border=colors[0], this_screen_border=colors[0], inactive=colors[0]),
				widget.TextBox(text='◣', background=colors[0], foreground=colors[1], fontsize=32, width=27, padding=-5),
                widget.WindowName(),
                widget.TextBox(text='◥', background=colors[0], foreground=colors[6], fontsize=32, width=27),
                Bluetooth(hci='dev_41_42_30_00_18_CD', format='  Bluetooth: {status}', background=colors[6], foreground=colors[-1], mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('bash /home/graeme/.local/bin/bluetooth.sh')}),
				widget.TextBox(text='◥', background=colors[6], foreground=colors[1], fontsize=32, width=27),
                widget.KeyboardLayout(fmt='  Keyboard: {}', background=colors[1], configured_keyboards=['us', 'es', 'gr']),
				widget.TextBox(text='◥', background=colors[1], foreground=colors[6], fontsize=32, width=27),
				widget.Battery(charge_char='+', discharge_char='-', full_char='', show_short_text=False, format='  Power: {char}{percent:2.0%}', background=colors[6]),
				widget.TextBox(text='◥', background=colors[6], foreground=colors[1], fontsize=32, width=27),
				widget.Volume(background=colors[1], fmt='  Volume: {}'),
				widget.TextBox(text='◥', background=colors[1], foreground=colors[6], fontsize=32, width=27),
                widget.CPU(background=colors[6], format='  CPU: {freq_current}GHz {load_percent}%'),
				widget.TextBox(text='◥', background=colors[6], foreground=colors[1], fontsize=32, width=27),
                widget.Memory(background=colors[1], fmt='  RAM: {}'),
                widget.TextBox(text='◥', background=colors[1], foreground=colors[6], fontsize=32, width=27),
                widget.Wlan(interface='wlp1s0', background=colors[6], disconnected_message='  Disconnected', format='  Network: {essid}'),
				widget.TextBox(text='◥', background=colors[6], foreground=colors[1], fontsize=32, width=27),
                widget.Clock(format='  %A, %B %d %H:%M ', background=colors[1]),
            ],
            20,
			background=colors[0],
        ),
        wallpaper=os.path.join(wallpaper_path, '284466.jpg')
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front())
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'

# hack to make java GUI work
wmname = 'LG3D'
