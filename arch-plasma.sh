#!/usr/bin/env bash

# Use this script after installing Arch Linux with Plasma Desktop Environment through the archinstall script.

echo -n "Update the system? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo pacman -Syu
fi

PACMAN_INSTALL_PACKAGES=(
    # Games
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
    ## Utilities
    neovim
    htop
    fastfetch
    github-cli
    distrobox
    # Etc
    noto-fonts-cjk
    noto-fonts-emoji
    flatpak
    fcitx5-hangul
    fcitx5-configtool
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
    ## Browsers
    brave-bin
    ## Development
    visual-studio-code-bin
)

echo -n "Install additional recommended AUR packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    yay -S "${AUR_INSTALL_PACKAGES[@]}"
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