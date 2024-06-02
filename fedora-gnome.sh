#!/usr/bin/env bash

echo -n "Update the system? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo dnf upgrade
fi


echo -n "Enable RPM Fusion? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
    sudo dnf config-manager --enable fedora-cisco-openh264
    sudo dnf update -y @core
fi

echo -n "Install additional packages for multimedia from RPM Fusion? (No VAAPI) [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo dnf swap -y ffmpeg-free ffmpeg --allowerasing
    sudo dnf update -y @multimedia --setopt="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
    sudo dnf update -y @sound-and-video
    sudo dnf install -y rpmfusion-free-release-tainted
    sudo dnf install -y libdvdcss
    sudo dnf install -y rpmfusion-nonfree-release-tainted
    sudo dnf --repo=rpmfusion-nonfree-tainted install -y "*-firmware"
fi

echo "[1] Intel(recent) [2] Intel(older) [3] AMD [4] NVIDIA [else] None"
echo -n "Select VAAPI driver to install [1/2/3/4/else]: "

read answer

case "$answer" in
    1)
        sudo dnf install -y intel-media-driver
        ;;
    2)
        sudo dnf install -y libva-intel-driver
        ;;
    3)
        sudo dnf swap -y mesa-va-drivers mesa-va-drivers-freeworld
        sudo dnf swap -y mesa-vdpau-drivers mesa-vdpau-drivers-freeworld
        sudo dnf swap -y mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686
        sudo dnf swap -y mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686
        ;;
    4)
        sudo dnf install -y libva-nvidia-driver
        ;;
    *)
        ;;
esac

DNF_INSTALL_PACKAGES=(
    # GUI
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

echo -n "Install Rustup? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
fi

echo -n "Install VSCode? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
    echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null
    dnf check-update -y
    sudo dnf install -y code
fi

echo -n "Install ProtonVPN? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    wget "https://repo.protonvpn.com/fedora-$(cat /etc/fedora-release | cut -d\  -f 3)-stable/protonvpn-stable-release/protonvpn-stable-release-1.0.1-2.noarch.rpm"
    sudo dnf install -y ./protonvpn-stable-release-1.0.1-2.noarch.rpm
    rm ./protonvpn-stable-release-1.0.1-2.noarch.rpm
    sudo dnf install -y --refresh proton-vpn-gnome-desktop
fi

DNF_REMOVE_PACKAGES=(
    firefox
    gnome-shell-extension-background-logo
    gnome-shell-extension-appindicator
)

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

echo -n "Install hugo(extended, v0.126.1)? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    mkdir tmp
    cd tmp
    wget https://github.com/gohugoio/hugo/releases/download/v0.126.1/hugo_extended_0.126.1_linux-amd64.tar.gz
    tar -xzf hugo_extended_0.126.1_linux-amd64.tar.gz
    sudo mv hugo /usr/local/bin
    cd ..
    rm -rf tmp
fi

echo -n "Remove unnecessary packages? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo dnf remove "${DNF_REMOVE_PACKAGES[@]}"
fi

echo -n "Add Flathub repository? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
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
    com.discordapp.Discord
    com.slack.Slack
    org.signal.Signal
    # Gaming
    com.mojang.Minecraft
)

echo -n "Install additional packages from Flathub? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    flatpak install flathub "${FLATPAK_INSTALL_PACKAGES[@]}"
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