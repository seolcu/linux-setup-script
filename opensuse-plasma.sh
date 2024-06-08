#!/usr/bin/env bash

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

echo -n "Update the system? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo zypper dup
fi

echo -n "Install additional packages for multimedia from Packman? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo zypper in opi
    opi codecs
fi

ZYPPER_INSTALL_PACKAGES=(
    # GUI
    ## Games
    steam
    ## Etc
    proton-vpn
    kvantum-manager

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

echo -n "Install VSCode? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
    echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ntype=rpm-md\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" |sudo tee /etc/zypp/repos.d/vscode.repo > /dev/null
    sudo zypper refresh
    sudo zypper install code
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

echo -n "Setup Fcitx5 environment variables? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo 'GTK_IM_MODULE=fcitx' | sudo tee -a /etc/environment
    echo 'QT_IM_MODULE=fcitx' | sudo tee -a /etc/environment
    echo 'XMODIFIERS=@im=fcitx' | sudo tee -a /etc/environment
fi

echo -n "Change hostname? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo -n "Enter new hostname: "
    read hostname
    sudo hostnamectl set-hostname "$hostname"
fi

echo -n "Add nord colorscheme to Konsole? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    mkdir -p ~/.local/share/konsole
    curl -o ~/.local/share/konsole/Nord.colorscheme https://raw.githubusercontent.com/nordtheme/konsole/develop/src/nord.colorscheme
fi

./common.sh
