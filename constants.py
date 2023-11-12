# Constants

DNF_PACKAGES: list[str] = [
    # GUI
    ## Browser
    "firefox-wayland",
    ## GNOME
    "gnome-extensions-app"
    ## Gaming
    "steam",
    ## Etc
    "solaar",
    # CLI
    ## Development
    ### C/C++
    "gcc",
    "g++",
    ### Java
    "java-latest-openjdk",
    ### Python
    "python3-ipykernel",
    "black",
    ## Utilities
    "htop",
    "neofetch",
    "gh",
    "distrobox",
    "neovim",
    # Plugins
    ## GNOME extensions
    "gnome-shell-extension-appindicator",
    "gnome-shell-extension-caffeine",
    "gnome-shell-extension-gsconnect",
    # Fonts
    "google-noto-sans-cjk-fonts",
]

FLATPAK_PACKAGES = [
    # GNOME Apps
    ## Circle
    "com.rafaelmardojai.Blanket",
    ## Etc
    "com.usebottles.bottles",
    # Work
    "org.onlyoffice.desktopeditors",
    "md.obsidian.Obsidian",
    # Communication
    "us.zoom.Zoom",
    # Utilities
    "com.github.unrud.VideoDownloader",
    "org.raspberrypi.rpi-imager",
    # Web
    # Games
    "com.discordapp.Discord",
    "com.mojang.Minecraft",
    # Etc
    "com.obsproject.Studio",
]
