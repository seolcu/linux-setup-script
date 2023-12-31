# Constants

DNF_PACKAGES: list[str] = [
    # GUI
    "gnome-tweaks",
    "chromium",
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
    "htop",
    "neofetch",
    "gh",
    "distrobox",
    # GNOME extensions
    "gnome-shell-extension-appindicator",
    "gnome-shell-extension-caffeine",
    "gnome-shell-extension-gsconnect",
    # Etc
    "hugo",
    "google-noto-sans-cjk-fonts",
]

DNF_REMOVE_PACKAGES: list[str] = [
    "firefox",
]


FLATPAK_PACKAGES: list[str] = [
    # Web Browsers
    "org.mozilla.firefox",
    # GNOME Apps
    "de.haeckerfelix.Fragments",
    ## Etc
    "com.mattjakeman.ExtensionManager",
    "com.belmoussaoui.Decoder",
    "com.usebottles.bottles",
    # Work
    "org.onlyoffice.desktopeditors",
    "md.obsidian.Obsidian",
    "us.zoom.Zoom",
    # Utilities
    "org.raspberrypi.rpi-imager",
    "org.videolan.VLC",
    # Games
    "com.valvesoftware.Steam",
    # Etc
    "com.obsproject.Studio",
]
