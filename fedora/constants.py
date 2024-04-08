# Constants

DNF_PACKAGES: list[str] = [
    # GUI
    "gnome-tweaks",
    # CLI
    ## Development
    ### C/C++
    "gcc",
    "g++",
    ### Java
    "java-17-openjdk-devel",
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
]

DNF_REMOVE_PACKAGES: list[str] = [
    "firefox",
    "rhythmbox",
]


FLATPAK_PACKAGES: list[str] = [
    # Web Browsers
    "com.brave.Browser",
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
    # Etc
    "com.obsproject.Studio",
    "org.gnome.NetworkDisplays",
]
