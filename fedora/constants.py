# Constants

DNF_PACKAGES: list[str] = [
    # GUI
    "chromium",
    "gnome-tweaks",
    "solaar",
    # CLI
    ## Development
    ### C/C++
    "gcc",
    "g++",
    ### Java
    "java-latest-openjdk-devel",
    ### Python
    "python3-pip",
    "python3-ipykernel",
    "black",
    ## Utilities
    "neovim",
    "htop",
    "neofetch",
    "gh",
    "distrobox",
    # GNOME extensions
    "gnome-shell-extension-appindicator",
    "gnome-shell-extension-caffeine",
    "gnome-shell-extension-gsconnect",
    # Etc
    "google-noto-sans-cjk-fonts",
    "ripgrep",
]

DNF_REMOVE_PACKAGES: list[str] = [
    "firefox",
    "rhythmbox",
]


FLATPAK_PACKAGES: list[str] = [
    # Web Browsers
    "org.mozilla.firefox",
    # GNOME Apps
    "de.haeckerfelix.Fragments",
    "org.gnome.SoundRecorder",
    ## Etc
    "com.mattjakeman.ExtensionManager",
    "com.belmoussaoui.Decoder",
    "com.usebottles.bottles",
    # Work
    "org.onlyoffice.desktopeditors",
    "md.obsidian.Obsidian",
    # Communication
    "us.zoom.Zoom",
    "com.discordapp.Discord",
    "com.slack.Slack",
    "org.signal.Signal",
    # Utilities
    "org.raspberrypi.rpi-imager",
    "org.videolan.VLC",
    "com.vixalien.decibels",
    # Games
    "com.valvesoftware.Steam",
    "com.mojang.Minecraft",
    # Etc
    "com.obsproject.Studio",
    "org.gnome.NetworkDisplays",
]
