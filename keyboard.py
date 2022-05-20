from libqtile.config import Key
from libqtile.lazy import lazy

terminal = "kitty"

def shortcuts(mod):
    return [
        # Navigation
        Key([mod], "h", lazy.layout.left()),
        Key([mod], "l", lazy.layout.right()),
        Key([mod], "j", lazy.layout.down()),
        Key([mod], "k", lazy.layout.up()),
        Key([mod, "control"], "space", lazy.layout.next()),

        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

        # Grow and shrink windows
        Key([mod, "control"], "h",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add()
            ),
        Key([mod, "control"], "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ration(),
            lazy.layout.delete()
            ),
        Key([mod, "control"], "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster()
            ),
        Key([mod, "control"], "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster
            ),
        Key([mod], "n", lazy.layout.normalize()),

        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout()),
        Key([mod], "q", lazy.window.kill()),
        Key([mod, "shift"], "r", lazy.reload_config()),
        Key([mod, "shift"], "q", lazy.shutdown()),

        # System stuff
        Key([mod], "x", lazy.spawn("arcolinux-logout")),
        Key([mod], "0", lazy.spawn("amixer set Master 10%+")),
        Key([mod], "9", lazy.spawn("amixer set Master 10%-")),
        Key([mod], "8", lazy.spawn("amixer -D pulse set Master 1+ toggle")),

        # Start applications
        Key([mod], "Return", lazy.spawn(terminal)),
        Key([mod], "w", lazy.spawn("firefox")),
        Key([mod], "e", lazy.spawn("dolphin")),
        Key([mod], "space", lazy.spawn("rofi -show drun")),
        Key([mod, "shift"], "space", lazy.spawn("rofi -show window")),
    ]

