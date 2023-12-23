# Constants

PACMAN_PACKAGES: list[str] = [
    # GUI
    "firefox",
    "chromium",
    "solaar",
    "gnome-boxes",
    "steam",
    "obs-studio",
    "fragments",
    # CLI
    ## Development
    ### C/C++
    "gcc",
    ### Java
    "jdk-openjdk",
    ### Python
    "python-ipykernel",
    "python-black",
    ### Node.js
    "nodejs",
    ### Hugo
    "hugo",
    ## Utilities
    "curl",
    "wget",
    "htop",
    "neofetch",
    "git",
    "github-cli",
    "distrobox",
    "neovim",
    ## Man
    "man-db",
    "man-pages",
    ## Fonts
    "noto-fonts-cjk",
    "noto-fonts-emoji",
    ## Korean Input
    "ibus-hangul",
    ## Printing
    "cups",
    "cups-pdf",
    ## Etc
    "texinfo",
    # Plugins
    ## GNOME
    "power-profiles-daemon",
    ## GNOME extensions
    "gnome-shell-extension-appindicator",
    "gnome-shell-extension-caffeine",
    ## Flatpak
    "flatpak",
]

AUR_PACKAGES: list[str] = [
    # GUI
    "visual-studio-code-bin",
    # Plugins
    ## GNOME extensions
    "gnome-shell-extension-gsconnect",
    "gnome-shell-extension-vitals",
]


FLATPAK_PACKAGES: list[str] = [
    # GNOME Apps
    "com.mattjakeman.ExtensionManager"
    ## Etc
    "com.belmoussaoui.Decoder",
    "com.usebottles.bottles",
    # Work
    "org.onlyoffice.desktopeditors",
    "md.obsidian.Obsidian",
    # Utilities
    "org.raspberrypi.rpi-imager",
]
