#!/usr/bin/env bash

./distro/opensuse.sh
./desktop/plasma.sh
./common-pre.sh

ZYPPER_REMOVE_PACKAGES=(
    *Firefox*
    *fcitx*
    *Fcitx*
    alee-fonts
    nanum-fonts
    nanum-gothic-coding-fonts
    un-fonts
    baekmuk-ttf-fonts
)

echo -n "Remove unnecessary packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo zypper remove "${ZYPPER_REMOVE_PACKAGES[@]}"
fi

ZYPPER_INSTALL_PACKAGES=(
    # GUI
    ## Games
    steam
    ## Etc
    proton-vpn
    kvantum-manager
    gnome-disk-utility

    # CLI
    ## Development
    ### Java
    java-21-openjdk-devel
    ### Python
    python311-ipykernel
    python311-black
    ### Node.js
    nodejs-default
    ## Utilities
    neovim
    htop
    fastfetch
    gh
    ## Hangul
    fcitx5-hangul
    fcitx5-configtool-kcm6
    ## Fonts
    google-noto-sans-cjk-fonts
    google-noto-sans-kr-fonts
    google-noto-serif-kr-fonts
    google-noto-sans-kr-mono-fonts
    jetbrains-mono-fonts
    ## Etc
    kdeconnect-kde
    starship
)

echo -n "Install additional recommended packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo zypper in "${ZYPPER_INSTALL_PACKAGES[@]}"
fi

FLATPAK_INSTALL_PACKAGES=(
    # Web Browsers
    com.brave.Browser
    # Work
    org.onlyoffice.desktopeditors
    md.obsidian.Obsidian
    com.obsproject.Studio
    # Communication
    us.zoom.Zoom
    com.slack.Slack
    org.signal.Signal
    com.discordapp.Discord
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

./common-post.sh