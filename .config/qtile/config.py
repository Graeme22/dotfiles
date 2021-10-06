import os
import random
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile import hook
from libqtile import qtile


@hook.subscribe.startup
def autostart():
    dunst = os.path.expanduser('~/.local/bin/launchdunst.sh')
    bus = os.path.expanduser('~/.local/bin/launchbus.sh')
    spotify = os.path.expanduser('~/.local/bin/launchspotifyd.sh')
    subprocess.call([dunst])
    subprocess.call([bus])
    subprocess.call([spotify])

    os.environ['DISPLAY'] = ':1'


wallpapers = []
wallpaper_path = '/home/graeme/.config/qtile/wallpapers'

for img in os.listdir(wallpaper_path):
    full_path = os.path.join(wallpaper_path, img)
    if os.path.isfile(full_path):
        wallpapers.append(img)

choice = random.choice(wallpapers)
wallpaper = os.path.join(wallpaper_path, choice)
os.system('wal -q -i ' + wallpaper)
colors = []

with open('/home/graeme/.cache/wal/colors', 'r') as file:
    for i in range(8):
        colors.append(file.readline().strip())
colors.append('#ffffff')

mod = 'mod4'

keys = [
    # move focus
    Key([mod], 'Left', lazy.layout.left()),
    Key([mod], 'Right', lazy.layout.right()),
    Key([mod], 'Up', lazy.layout.up()),
    Key([mod], 'Down', lazy.layout.down()),

    # move windows
    Key([mod, 'control'], 'Left', lazy.layout.shuffle_left()),
    Key([mod, 'control'], 'Right', lazy.layout.shuffle_right()),
    Key([mod, 'control'], 'Up', lazy.layout.shuffle_up()),
    Key([mod, 'control'], 'Down', lazy.layout.shuffle_down()),

    # resize windows
    Key([mod, 'shift'], 'Left', lazy.layout.grow_left()),
    Key([mod, 'shift'], 'Right', lazy.layout.grow_right()),
    Key([mod, 'shift'], 'Up', lazy.layout.grow_up()),
    Key([mod, 'shift'], 'Down', lazy.layout.grow_down()),

    # Switch window focus to other pane(s) of stack
    #Key([mod], 'space', lazy.layout.next(), desc='Switch window focus to other pane(s) of stack'),

    # quick launch
    Key([mod], 'Return', lazy.spawn('alacritty'), desc='Launch terminal'),
    Key([mod], 'b', lazy.spawn('chromium')),

    # Toggle between different layouts as defined below
    #Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),

	# launcher
    Key([mod], 'r', lazy.spawn('wofi')),
    #Key([mod], 'r', lazy.spawn('bash /home/graeme/.config/rofi/launchers/colorful/launcher.sh')),

    # restart
    Key([mod, 'shift'], 'r', lazy.restart(), desc='Restart qtile'),

    # Volume control
	Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer sset Master 5%+ unmute')),
	Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer sset Master 5%- unmute')),
	Key([], 'XF86AudioMute', lazy.spawn('amixer -q set Master toggle')),

	# Brightness
	Key([], 'XF86MonBrightnessUp', lazy.spawn('blight set +5%')),
	Key([], 'XF86MonBrightnessDown', lazy.spawn('blight set -5%')),

	# lock screen / power off / reboot
    Key([mod], 'l', lazy.spawn('swaylock -i ' + wallpaper)),
	#Key([mod], 'l', lazy.spawn('betterlockscreen --lock blur')),
    Key([mod, 'shift'], 'q', lazy.shutdown()),

    # screenshot
    Key([mod], 'x', lazy.spawn('grim')),

    # keyboard
    Key([mod], 'k', lazy.widget['keyboardlayout'].next_keyboard(), desc='Next keyboard layout'),
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
	'border_width': 2,
	'border_focus': colors[1],
	'margin': 5,
    'lower_right': False,
}

layouts = [
    layout.Bsp(**layout_cfg),
]

widget_defaults = dict(
    font='hack',
    fontsize=14,
	foreground=colors[-1],
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(fmt=' {} ', background=colors[1], this_current_screen_border=colors[0], this_screen_border=colors[0], inactive=colors[0]),
                widget.WindowName(format=' {state}{name} '),
                #widget.Bluetooth(hci='/dev_41_42_30_00_18_CD', fmt=' Bluetooth: {} ', background=colors[6]),
                widget.KeyboardLayout(fmt=' Keyboard: {} ', background=colors[1], configured_keyboards=['us', 'es']),
				widget.Battery(charge_char='+', discharge_char='-', full_char='', show_short_text=False, format=' Power: {char}{percent:2.0%} ', background=colors[6], notify_below=10),
				widget.Volume(background=colors[1], fmt=' Volume: {} '),
                widget.CPU(background=colors[6], format=' CPU: {freq_current}GHz {load_percent}% '),
                widget.Memory(background=colors[1], fmt=' RAM: {} '),
                widget.Wlan(interface='wlan0', background=colors[6], disconnected_message=' Disconnected ', format=' Network: {essid} '),
                widget.Clock(format=' %A, %B %d %H:%M ', background=colors[1]),
            ],
            20,
			background=colors[0],
        ),
        wallpaper=wallpaper
    )
]

# Drag floating layouts.
mouse = []

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
