#!/usr/bin/env bash

./distro/fedora.sh
./desktop/gnome.sh
./common.sh

DNF_INSTALL_PACKAGES=(
    # GUI
    ## Work
    discord
    ## GNOME Apps
    gnome-tweaks
    ## Games
    steam

    # CLI
    ## Development
    ### C/C++
    gcc
    g++
    ### Java
    java-21-openjdk-devel
    ### Python
    python3-pip
    python3-ipykernel
    black
    ### Node.js
    nodejs
    ## Utilities
    neovim
    htop
    fastfetch
    gh
    distrobox
    # GNOME extensions
    ## AppIndicator and KStatusNotifierItem Support Dependencies
    libappindicator
    ## GSConnect Dependencies
    openssl
    nautilus-python
    nautilus-extensions
    ## Vitals Dependencies
    libgtop2-devel
    lm_sensors
    # Etc
    google-noto-sans-cjk-fonts
)

echo -n "Install additional recommended packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo dnf install "${DNF_INSTALL_PACKAGES[@]}"
fi

DNF_REMOVE_PACKAGES=(
    firefox
    gnome-shell-extension-background-logo
    gnome-shell-extension-appindicator
)

echo -n "Remove unnecessary packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo dnf remove "${DNF_REMOVE_PACKAGES[@]}"
fi

FLATPAK_INSTALL_PACKAGES=(
    # Web Browsers
    com.brave.Browser
    # GNOME Apps
    com.mattjakeman.ExtensionManager
    # Work
    org.onlyoffice.desktopeditors
    md.obsidian.Obsidian
    # Communication
    us.zoom.Zoom
    com.slack.Slack
    org.signal.Signal
    # Gaming
    org.prismlauncher.PrismLauncher
    # Utilities
    com.usebottles.bottles
)

echo -n "Install additional packages from Flathub? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    flatpak install flathub "${FLATPAK_INSTALL_PACKAGES[@]}"
fi
