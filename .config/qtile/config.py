# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from bluetooth import Bluetooth

mod = "mod4"

keys = [
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),

    # quick launch
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("brave")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),

	# rofi launcher
    Key([mod], "r", lazy.spawn("bash /home/graeme/.config/rofi/launchers/misc/launcher.sh")),

	# Volume control
	Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+ unmute")),
	Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%- unmute")),
	Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),

	# Brightness
	Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
	Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),

	# lock screen / power off / reboot
	Key([mod], "l", lazy.spawn("betterlockscreen --lock blur")),
    Key([mod], "q", lazy.spawn("systemctl poweroff")),

    # keyboard layouts
    Key([mod], "k", lazy.spawn("bash /home/graeme/.local/bin/togglekeyboard.sh")),

    # screenshot
    Key([mod], "x", lazy.spawn("scrot '%Y-%m-%d_$wx$h_scrot.png' -e 'mv $f ~/Pictures'")),
]

groups = [Group(i) for i in "asdf"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

colors = {
    'black': '#131a17',
    'blue': '#699AAA',
    'grey': '#929FA8',
    'cream': '#C5C2B1',
    'white': '#cadeea',
	'green': '#137866',
}

layout_cfg = {
	'border_width': 2,
	'border_focus': colors['blue'],
	'margin': 8,
}

layouts = [
    layout.Max(**layout_cfg),
    layout.MonadTall(**layout_cfg),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
	foreground=colors['black'],
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(background=colors['green']),
                widget.Spacer(length=5, background=colors['green']),
				widget.TextBox(text='◣', background=colors['blue'], foreground=colors['green'], fontsize=32, width=27, padding=-5),
                widget.GroupBox(background=colors['blue'], this_current_screen_border=colors['black'], this_screen_border=colors['black'], inactive=colors['black']),
				widget.TextBox(text='◣', background=colors['black'], foreground=colors['blue'], fontsize=32, width=27, padding=-5),
                widget.WindowName(foreground=colors['white']),
				widget.Spacer(),
                widget.TextBox(text='◥', background=colors['black'], foreground=colors['green'], fontsize=32, width=27),
                Bluetooth(format='  Bluetooth: {status}', background=colors['green'], foreground=colors['white']),
				widget.TextBox(text='◥', background=colors['green'], foreground=colors['blue'], fontsize=32, width=27),
                widget.KeyboardLayout(fmt='  Keyboard: {}', background=colors['blue']),
				widget.TextBox(text='◥', background=colors['blue'], foreground=colors['green'], fontsize=32, width=27),
				widget.Battery(charge_char='+', discharge_char='-', format='  Power: {char}{percent:2.0%}', background=colors['green'], foreground=colors['white']),
				widget.TextBox(text='◥', background=colors['green'], foreground=colors['blue'], fontsize=32, width=27),
				widget.Volume(background=colors['blue'], fmt='  Volume: {}'),
				widget.TextBox(text='◥', background=colors['blue'], foreground=colors['green'], fontsize=32, width=27),
                widget.CPU(background=colors['green'], format='  CPU: {freq_current}GHz {load_percent}%', foreground=colors['white']),
				widget.TextBox(text='◥', background=colors['green'], foreground=colors['blue'], fontsize=32, width=27),
                widget.Memory(background=colors['blue'], fmt='  RAM: {}'),
                widget.TextBox(text='◥', background=colors['blue'], foreground=colors['green'], fontsize=32, width=27),
                widget.Wlan(interface='wlp1s0', background=colors['green'], format='  Network: {essid}', foreground=colors['white']),
				widget.TextBox(text='◥', background=colors['green'], foreground=colors['blue'], fontsize=32, width=27),
                widget.Clock(format='  %A, %B %d %H:%M ', background=colors['blue']),
            ],
            20,
			background=colors['black'],
        ),
		wallpaper='/home/graeme/.config/qtile/wallpaper.jpg',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
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
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "qtile"
