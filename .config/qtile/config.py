import os
import subprocess

from libqtile import bar, hook, widget
from libqtile.config import Group, Key, Screen
from libqtile.layout import Bsp, MonadWide
from libqtile.lazy import lazy

WALLPAPER_PATH = "/home/graeme/.config/qtile/wallpapers/shaded_landscape.png"


@hook.subscribe.startup
def autostart():
    kp = os.path.expanduser("~/.local/bin/keepass.sh")
    dunst = os.path.expanduser("~/.local/bin/dunst.sh")
    xkb = os.path.expanduser("~/.local/bin/xkb.sh")
    subprocess.call([kp])
    subprocess.call([dunst])
    subprocess.call([xkb])


colors = []
with open("/home/graeme/.colors", "r") as file:
    for i in range(8):
        colors.append(file.readline().strip())

mod = "mod1"

keys = [
    # move focus
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    # move windows
    Key([mod, "control"], "h", lazy.layout.shuffle_left()),
    Key([mod, "control"], "l", lazy.layout.shuffle_right()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    # resize windows
    Key([mod, "shift"], "h", lazy.layout.grow_left()),
    Key([mod, "shift"], "l", lazy.layout.grow_right()),
    Key([mod, "shift"], "k", lazy.layout.grow_up()),
    Key([mod, "shift"], "j", lazy.layout.grow_down()),
    # quick launch
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("chromium")),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    # launcher
    Key(
        [mod],
        "r",
        lazy.spawn("bash /home/graeme/.config/rofi/launchers/misc/launcher.sh"),
    ),
    # restart
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    # Volume control
    Key([mod], "plus", lazy.spawn("pactl -- set-sink-volume 0 +5%")),
    Key([mod], "minus", lazy.spawn("pactl -- set-sink-volume 0 -5%")),
    Key([mod], "period", lazy.spawn("pactl set-sink-mute 0 toggle")),
    # Brightness
    Key([mod, "shift"], "plus", lazy.spawn("ddcutil setvcp 10 + 10")),
    Key([mod, "shift"], "minus", lazy.spawn("ddcutil setvcp 10 - 10")),
    # lock screen / power off / reboot
    Key([mod, "shift"], "l", lazy.spawn("i3lock -i " + WALLPAPER_PATH)),
    # Key([mod], 'l', lazy.spawn('betterlockscreen --lock blur')),
    Key([mod, "shift"], "q", lazy.shutdown()),
    # screenshot
    Key([mod], "x", lazy.spawn("scrot")),
    # keyboard
    # Key([mod], 'k', lazy.widget['keyboardlayout'].next_keyboard(), desc='Next keyboard layout'),
]

groups = [Group(i) for i in "asdf"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_cfg = {
    "border_width": 2,
    "border_focus": colors[1],
    "margin": 5,
    "lower_right": False,
}

layouts = [
    Bsp(**layout_cfg),
    MonadWide(**layout_cfg),
]

widget_defaults = dict(
    font="hack",
    fontsize=14,
    foreground=colors[-1],
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fmt=" {} ",
                    background=colors[1],
                    this_current_screen_border=colors[0],
                    this_screen_border=colors[0],
                    inactive=colors[0],
                ),
                widget.WindowName(format=" {state}{name} "),
                # widget.Bluetooth(hci='/dev_41_42_30_00_18_CD', fmt=' Bluetooth: {} ', background=colors[6]),
                # widget.KeyboardLayout(fmt=' Keyboard: {} ', background=colors[6], configured_keyboards=['latam', 'us']),
                # widget.Battery(charge_char='+', discharge_char='-', full_char='', show_short_text=False, format=' Power: {char}{percent:2.0%} ', background=colors[6], notify_below=10),
                widget.PulseVolume(
                    background=colors[1],
                    fmt=" Volume: {} ",
                    volume_app="pactl",
                    update_interval=0.2,
                    check_mute_command="pactl get-sink-mute 0",
                    get_volume_command="pactl get-sink-volume 0",
                ),
                widget.CPU(
                    background=colors[6],
                    format=" CPU: {freq_current}GHz {load_percent}% ",
                ),
                widget.Memory(background=colors[1], fmt=" RAM: {} "),
                widget.NvidiaSensors(background=colors[6], format=" GPU: {temp}°C "),
                widget.Wlan(
                    interface="wlan1",
                    background=colors[1],
                    disconnected_message=" Disconnected ",
                    format=" Network: {essid} ",
                ),
                widget.Clock(format=" %A, %B %d %H:%M ", background=colors[6]),
            ],
            20,
            background=colors[0],
        ),
        # wallpaper=wallpaper
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
focus_on_window_activation = "smart"

# hack to make java GUI work
wmname = "qtile"
