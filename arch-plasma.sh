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
    ## Work
    onlyoffice-bin
    zoom
    slack-desktop
    ## Games
    prismlauncher
    # Etc
    proton-vpn-gtk-app
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

echo -n "Install Rustup? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
fi

echo -n "Install Proton-GE with asdf? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.0
    echo '. "$HOME/.asdf/asdf.sh"' >> ~/.bashrc
    echo '. "$HOME/.asdf/completions/asdf.bash"' >> ~/.bashrc
    source ~/.bashrc
    asdf plugin add protonge
    asdf install protonge latest
fi

echo -n "Apply git configuration? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo -n "Enter your name: "
    read name
    echo -n "Enter your email: "
    read email
    git config --global user.name "$name"
    git config --global user.email "$email"
    git config --global init.defaultBranch main
    git config --global push.autoSetupRemote true
fi