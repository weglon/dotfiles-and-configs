# Zeke's Qtile config Based on the arcolinux default config.
# github.com/weglon/

import os
import re
import socket
import subprocess
from typing import List
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
from libqtile.widget import Spacer

FONT_SIZE = 15
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

@lazy.function
def window_to_prev_group(qtile):
  if qtile.currentWindow is not None:
    i = qtile.groups.index(qtile.currentGroup)
    qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
  if qtile.currentWindow is not None:
    i = qtile.groups.index(qtile.currentGroup)
    qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [
  # SUPER + FUNCTION KEYS
  Key([mod], "f", lazy.window.toggle_fullscreen()),
  Key([mod], "q", lazy.window.kill()),

  # SUPER + SHIFT KEYS
  Key([mod, "shift"], "r", lazy.restart()),

  # QTILE LAYOUT KEYS
  Key([mod, "shift"], "n", lazy.layout.normalize()),
  Key(["mod1"], "space", lazy.next_layout()),

  # CHANGE FOCUS
  Key([mod], "k", lazy.layout.up()),
  Key([mod], "j", lazy.layout.down()),
  Key([mod], "h", lazy.layout.left()),
  Key([mod], "l", lazy.layout.right()),


  # SIZE UP, DOWN, LEFT, RIGHT
  Key([mod, "control"], "l",
    lazy.layout.grow_right(),
    lazy.layout.grow(),
    lazy.layout.increase_ratio(),
    lazy.layout.delete(),
  ),
  Key([mod, "control"], "h",
    lazy.layout.grow_left(),
    lazy.layout.shrink(),
    lazy.layout.decrease_ratio(),
    lazy.layout.add(),
  ),
  Key([mod, "control"], "k",
    lazy.layout.grow_up(),
    lazy.layout.grow(),
    lazy.layout.decrease_nmaster(),
  ),
  Key([mod, "control"], "j",
    lazy.layout.grow_down(),
    lazy.layout.shrink(),
    lazy.layout.increase_nmaster(),
  ),

  # FlIP LAYOUT
  Key([mod, "shift"], "f", lazy.layout.flip()),

]

groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7"]
# group_labels = ["", "", "", "", "阮", "", ""]
group_labels = ["", "", "", "", "", "", ""]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

for i in range(len(group_names)):
  groups.append(
    Group(
      name=group_names[i],
      layout=group_layouts[i].lower(),
      label=group_labels[i],
    ))

for i in groups:
  keys.extend([
    # CHANGE WORKSPACES
    Key([mod], i.name, lazy.group[i.name].toscreen()),
    Key([mod], "Tab", lazy.screen.next_group()),
    Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
    Key(["mod1"], "Tab", lazy.screen.next_group()),
    Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

    # MOVE WINDOW TO SELECTED WORKSPACE
    Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
  ])


BACKGROUND_COLOR = "#1f1f1f";
BACKGROUND_HL_COLOR_DARK = "#0f0f0f";
BACKGROUND_HL_COLOR = "#2f2f2f";
FOREGROUND_COLOR = "#cccccc";

RED_COLOR = "#a86d5d";
GREEN_COLOR = "#80a85d";
PURPLE_COLOR = "#8d5da8";
BLUE_COLOR = "#5d7ca8";
CYAN_COLOR = "#83ccca";

def init_layout_theme():
  return {
    "margin":5,
    "border_width":5,
    "border_focus": BACKGROUND_COLOR,
    "border_normal": BACKGROUND_HL_COLOR
  }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Floating(**layout_theme),
]

# WIDGETS FOR THE BAR

def init_widgets_defaults():
  return dict(
    font="Caskaydia Cove Nerd Font",
    fontsize = FONT_SIZE,
    background=BACKGROUND_COLOR
  )

widget_defaults = init_widgets_defaults()

def init_widgets_list():
  prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
  widgets_list = [
    widget.Sep(
      linewidth=0,
      padding=3
    ),
    widget.GroupBox(
      fontsize = FONT_SIZE-1,
      margin_y = 3,
      margin_x = 0,
      padding_y = 6,
      padding_x = 20,
      borderwidth = 0,
      disable_drag = True,
      active = BACKGROUND_HL_COLOR,
      inactive = BACKGROUND_HL_COLOR_DARK,
      rounded = True,
      highlight_method = "text",
      this_current_screen_border = CYAN_COLOR,
      background = BACKGROUND_COLOR,
    ),
    widget.Sep(
      padding = 517,
      linewidth = 0
    ),
    widget.TextBox(
      text = "",
      foreground = RED_COLOR,
      fontsize = FONT_SIZE+3
    ),
    widget.Clock(
      foreground = FOREGROUND_COLOR,
      fontsize = FONT_SIZE,
      format="%d/%m/%y - %H:%M"
    ),
    widget.Sep(
      linewidth=0,
      padding=5
    ),
    #widget.CurrentLayout(
    #  foreground = COLOR_2,
    #),
    #widget.Sep(
    #  linewidth=0,
    #  padding=5
    #),
    widget.WindowName(
      format="{}",
      foreground = BACKGROUND_COLOR,
      background = BACKGROUND_COLOR,
    ),
    widget.TextBox(
      text="",
      FONT_SIZE=FONT_SIZE+4,
      foreground=PURPLE_COLOR
    ),
    widget.Memory(
      measure_mem = "M", 
      format = "{MemUsed: .0f} MiB",
      foreground = FOREGROUND_COLOR
    ),
    widget.Sep(
      linewidth=0,
      padding=5
    ),
    widget.TextBox(
      text="",
      fontsize=FONT_SIZE+5,
      foreground=GREEN_COLOR
    ),
    widget.CPU(
      format = "{load_percent}%",
      foreground = FOREGROUND_COLOR
    ),
    widget.Sep(
      linewidth=0,
      padding=5
    ),
    widget.TextBox(
      text="",
      fontsize=FONT_SIZE+3,
      foreground=BLUE_COLOR
    ),
    widget.DF(
      foreground = FOREGROUND_COLOR,
      visible_on_warn = False,
      format = "{uf} GB"
    ),
    #widget.Systray(
    #  background=BACKGROUND_COLOR,
    #  icon_size=15,
    #  padding = 10,
    #),
    widget.Sep(
      linewidth=0,
      padding=10
    )
  ]
  return widgets_list


widgets_list = init_widgets_list()
def init_widgets_screen1():
  widgets_screen1 = init_widgets_list()
  return widgets_screen1

def init_widgets_screen2():
  widgets_screen2 = init_widgets_list()
  return widgets_screen2
widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()

def init_screens():
  return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=32, opacity=0.8, margin=5))]
screens = init_screens()

# MOUSE CONFIGURATION
mouse = [
  Drag(
    [mod], "Button1", lazy.window.set_position_floating(),
    start=lazy.window.get_position()
  ),
  Drag(
    [mod], "Button3", lazy.window.set_size_floating(),
    start=lazy.window.get_size()
  )
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
#@hook.subscribe.client_new
#def assign_app_group(client):
# d = {}
# d[group_names[0]] = ["Atom", "Subl","code-oss", "Code", "code", "jetbrains-idea-ce"]
# d[group_names[1]] = ["Alacritty", "xfce-terminal"]
# d[group_names[2]] = ["Navigator", "firefox", "google-chrome", "chromium"]
# d[group_names[3]] = ["discord", "Skype", "skype"]
# d[group_names[4]] = ["minecraft-launcher", "Minecraft Launcher", "spotify", "Spotify", "Pragha", "Clementine", "Vlc", "vlc", "Mpv", "mpv"]
# d[group_names[5]] = ["Gimp", "gimp", "krita", "inkscape", "kdenlive"]
# d[group_names[6]] = ["Thunar", "Nemo", "Caja", "Pcmanfm", "Pcmanfm-qt", "thunar"]
#
# wm_class = client.window.get_wm_class()[0]
# for i in range(len(d)):
#   if wm_class in list(d.values())[i]:
#     group = list(d.keys())[i]
#     client.togroup(group)
#     client.group.cmd_toscreen(toggle=False)
#
main = None

@hook.subscribe.startup_once
def start_once():
  home = os.path.expanduser('~')
  subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
  # Set the cursor to something sane in X
  subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
  if (window.window.get_wm_transient_for() or window.window.get_wm_type() in floating_types):
    window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
  # Run the utility of `xprop` to see the wm class and name of an X client.
  *layout.Floating.default_float_rules, 
  Match(wm_class='confirmreset'),  # gitk
  Match(wm_class='makebranch'),  # gitk
  Match(wm_class='maketag'),  # gitk
  Match(wm_class='ssh-askpass'),  # ssh-askpass
  Match(title='branchdialog'),  # gitk
  Match(title='pinentry'),  # GPG key password entry
  Match(wm_class='Arcolinux-welcome-app.py'),
  Match(wm_class='Arcolinux-tweak-tool.py'),
  Match(wm_class='Arcolinux-calamares-tool.py'),
  Match(wm_class='confirm'),
  Match(wm_class='dialog'),
  Match(wm_class='download'),
  Match(wm_class='error'),
  Match(wm_class='file_progress'),
  Match(wm_class='notification'),
  Match(wm_class='splash'),
  Match(wm_class='toolbar'),
  Match(wm_class='Arandr'),
  Match(wm_class='feh'),
  Match(wm_class='Galculator'),
  Match(wm_class='arcolinux-logout'),
  Match(wm_class='xfce4-terminal'),
],
fullscreen_border_width = 0, border_width = 0)

auto_fullscreen = True
focus_on_window_activation = "focus" # or smart
wmname = "LG3D"
