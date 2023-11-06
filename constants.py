# Constants

APT_PACKAGES: list[str] = [
    # GUI
    ## Development
    ## Etc
    "timeshift",
    "solaar",
    "obs-studio",
    "steam-installer",
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
    ### Ruby
    "ruby-full",
    "bundler",
    "jekyll",
    ## Utilities
    "curl",
    "wget",
    "htop",
    "neofetch",
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
    "gnome-software-plugin-flatpak",
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
]
