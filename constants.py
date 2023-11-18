# Constants

APT_PACKAGES: list[str] = [
    # GUI
    "solaar",
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
    ## Etc
    "steam-devices",
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
    "com.valvesoftware.Steam",
    "com.discordapp.Discord",
    "com.mojang.Minecraft",
    # Etc
    "com.obsproject.Studio",
]
