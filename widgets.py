import themes

from libqtile import widget

theme = themes.current_theme
font_size = themes.font_size
icon_size = themes.icon_size

def windowNameParse(text): 
    for string in [
            "Chromium",
            "Firefox",
            "~",
            "Dolphin",
            "GNU Image Manipulation Program",
            "GIMP"]:
        if string in text and string == "~":
            if text[0] == "v":
                text = " Vim -" + text[1:len(text)]
            else:
                text = " Kitty - " + text
        elif string in text and string == "Firefox":
            # Just grab the page name without description name
            pn_beg = text.rfind("-")+1
            pn_end = text.find("—")
            pagename = text[pn_beg:pn_end]
            text = " Firefox - "+ pagename 
        elif string in text and string == "Dolphin":
            text = "  " + text
        elif string in text and (string == "GNU Image Manipulation Program" or string == "GIMP"):
            text = " GNU Image Manipulation Program"
        else:
            text = text

    return text

widget_list = [
        widget.Wallpaper(
            directory = "~/Pictures/Wallpapers/"+theme.wallpaper_dir,
            random_selection = True,
            wallpaper_command = ["feh" ,"--bg-fill"],
            label = ""
        ),
        widget.CurrentLayoutIcon(
            foreground = theme.foreground_dark,
            custom_icon_paths = ["/home/vespan/.config/qtile/layout-icon-themes/gruvbox-faded_green"],
            padding = 15,
            scale = 0.62
            ),
        widget.Sep(
            linewidth = 2,
            padding = 10,
            foreground = theme.background_dark
            ),
        widget.GroupBox(
            active = theme.foreground_dark,
            inactive = theme.background_light,
            highlight_method = "text",
            font = "Monoid Nerd Font",
            this_current_screen_border = theme.foreground,
            fontsize = font_size
            ),
        widget.Sep(
            linewidth = 2,
            foreground = theme.background_dark,
            padding = 15
            ),
        widget.Sep(linewidth = 0, padding = 10),
        widget.WindowName(
            format = "{name}",
            parse_text = windowNameParse,
            foreground = theme.windowname,
            fontsize = themes.font_size
            ),
        widget.TextBox(
            text="",
            FONT_SIZE=icon_size,
            foreground=theme.ram
            ),
        widget.Memory(
            measure_mem = "M", 
            format = "{MemUsed: .0f} MiB",
            foreground = theme.foreground
            ),
        widget.Sep(
            linewidth = 2,
            foreground = theme.background_dark,
            padding = 15
            ),
        widget.TextBox(
            text="",
            fontsize=icon_size,
            foreground=theme.cpu
            ),
        widget.CPU(
            format = "{load_percent}%",
            foreground = theme.foreground
            ),
        widget.Sep(
            linewidth = 2,
            padding = 15,
            foreground = theme.background_dark
            ),
        widget.TextBox(
            text = "望",
            fontsize = icon_size-1,
            foreground = theme.weather
            ),
        widget.Wttr(
            foreground=theme.foreground,
            location={'Stockholm': 'Stockholm'},
            format="%C %t"
            ),
        widget.Sep(
            linewidth = 2,
            padding = 15,
            foreground = theme.background_dark
            ),
        widget.TextBox(
            text = "",
            fontsize = icon_size,
            foreground = theme.clock
            ),
        widget.Clock(
            format = "%d/%m/%y - %H:%M",
            foreground = theme.foreground 
            ),
        widget.Sep(
            linewidth = 2,
            padding = 15,
            foreground = theme.background_dark
            ),
        widget.TextBox(
            text = "墳",
            fontsize = icon_size,
            foreground = theme.volume
            ),
        widget.Volume(
            foreground = theme.foreground,
            ),
        widget.Sep(
            padding = 15,
            linewidth = 0
            ),
       ]
  
