#!/usr/bin/env bash

# Use this script after installing Arch Linux with Plasma Desktop Environment through the archinstall script.

./distro/arch.sh
./desktop/plasma.sh
./common-pre.sh

PACMAN_INSTALL_PACKAGES=(
    # GUI
    ## Work
    obsidian
    discord
    signal-desktop
    obs-studio
    ## Virtualization
    virt-manager
    qemu-full
    dnsmasq
    ## Games
    steam

    # CLI
    ## Development
    ### C/C++
    gcc
    ### Java
    jdk-openjdk
    ### Python
    python-pip
    python-ipykernel
    python-black
    ### Node.js
    nodejs
    ### Hugo
    hugo
    ## Utilities
    curl
    wget
    neovim
    htop
    fastfetch
    github-cli
    distrobox
    ## Man
    man-db
    man-pages
    ## Printing
    cups
    cups-pdf
    ## Fonts
    noto-fonts-cjk
    noto-fonts-emoji
    ttf-jetbrains-mono
    ttf-jetbrains-mono-nerd
    ## Filesystem
    btrfs-progs
    dosfstools
    exfatprogs
    f2fs-tools
    ntfs-3g
    xfsprogs
    udftools
    # Etc
    texinfo
    flatpak
    fcitx5-hangul
    fcitx5-configtool
    power-profiles-daemon
    kdeconnect
    starship
)

echo -n "Install additional recommended packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo pacman -S "${PACMAN_INSTALL_PACKAGES[@]}"
fi

AUR_INSTALL_PACKAGES=(
    # GUI
    brave-bin
    ## Development
    visual-studio-code-bin
    # Etc
    proton-vpn-gtk-app
)

echo -n "Install additional recommended AUR packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    yay -S "${AUR_INSTALL_PACKAGES[@]}"
fi

FLATPAK_INSTALL_PACKAGES=(
    # Work
    org.onlyoffice.desktopeditors
    us.zoom.Zoom
    com.slack.Slack
    # Games
    com.mojang.Minecraft
    # Utilities
    com.usebottles.bottles
)

echo -n "Install additional recommended Flatpak packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    flatpak install flathub "${FLATPAK_INSTALL_PACKAGES[@]}"
fi

./common-post.sh