# Constants

APT_PACKAGES: list[str] = [
    # GUI
    "chromium",
    "solaar",
    "gnome-boxes",
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
    ### Node.js
    "nodejs",
    ## Utilities
    "curl",
    "wget",
    "htop",
    "neofetch",
    "git",
    "gh",
    "distrobox",
    # Plugins
    ## GNOME extensions
    "gnome-shell-extension-appindicator",
    "gnome-shell-extension-caffeine",
    "gnome-shell-extension-gamemode",
    "gnome-shell-extension-gsconnect",
    ## Flatpak
    "flatpak",
    "gnome-software-plugin-flatpak",
    ## Etc
    "hugo",
]


APT_REMOVE_PACKAGES: list[str] = [
    "gnome-games",
    "file-roller",
]

FLATPAK_PACKAGES: list[str] = [
    # GNOME Apps
    ## Etc
    "com.belmoussaoui.Decoder",
    "com.usebottles.bottles",
    # Work
    "org.onlyoffice.desktopeditors",
    "md.obsidian.Obsidian",
    # Utilities
    "org.raspberrypi.rpi-imager",
    # Games
    "com.valvesoftware.Steam",
    # Etc
    "com.obsproject.Studio",
]
