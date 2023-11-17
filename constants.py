# Constants

APT_PACKAGES: list[str] = [
    # GUI
    ## GNOME
    "gnome-extensions-app",
    ## Gaming
    "steam-installer",
    ## Etc
    "solaar",
    "obs-studio",
    # CLI
    ## Development
    ### C/C++
    "gcc",
    "g++",
    ### Java
    "default-jdk",
    ### Python
    "python3-pip",
    "python3-venv",
    "python3-ipykernel",
    "black",
    ## Utilities
    "curl",
    "wget",
    "htop",
    "neofetch",
    "git",
    "gh",
    "distrobox",
    "neovim",
    # Plugins
    ## GNOME extensions
    "gnome-shell-extension-appindicator",
    "gnome-shell-extension-caffeine",
    "gnome-shell-extension-gamemode",
    "gnome-shell-extension-gsconnect",
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
    # Games
    "com.discordapp.Discord",
    "com.mojang.Minecraft",
]
