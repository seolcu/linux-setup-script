#!/usr/bin/env bash

# Use this script after installing Arch Linux with Plasma Desktop Environment through the archinstall script.

echo -n "Update the system? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo pacman -Syu
fi

PACMAN_INSTALL_PACKAGES=(
    # GUI
    ## Work
    obsidian
    discord
    signal-desktop
    obs-studio
    gnome-boxes
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
    # Etc
    texinfo
    flatpak
    fcitx5-hangul
    fcitx5-configtool
    power-profiles-daemon
    kdeconnect
)

echo -n "Install additional recommended packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo pacman -S "${PACMAN_INSTALL_PACKAGES[@]}"
fi

echo -n "Install AUR helper? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    git clone https://aur.archlinux.org/yay-bin.git
    cd yay-bin
    makepkg -si
    cd ..
    rm -rf yay-bin
fi

AUR_INSTALL_PACKAGES=(
    # GUI
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
    # Web Browsers
    com.brave.Browser
    # Work
    org.onlyoffice.desktopeditors
    us.zoom.Zoom
    com.slack.Slack
    # Games
    org.prismlauncher.PrismLauncher
    # Utilities
    com.usebottles.bottles
)

echo -n "Install additional recommended Flatpak packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    flatpak install flathub "${FLATPAK_INSTALL_PACKAGES[@]}"
fi

echo -n "Setup Fcitx5 environment variables? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo 'GTK_IM_MODULE=fcitx' | sudo tee -a /etc/environment
    echo 'QT_IM_MODULE=fcitx' | sudo tee -a /etc/environment
    echo 'XMODIFIERS=@im=fcitx' | sudo tee -a /etc/environment
fi

echo -n "Enable Bluetooth service? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo systemctl enable --now bluetooth
fi

./common.sh