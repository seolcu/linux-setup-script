#!/usr/bin/env bash

echo -n "Update the system? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo dnf upgrade
fi

echo -n "Add Flathub repository? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
    sudo flatpak remote-modify flathub --enable
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

echo -n "Install Starship.rs? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    curl -sS https://starship.rs/install.sh | sh
fi

echo -n "Install JetBrainsMono Nerd Font? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    mkdir -p ~/.local/share/fonts
    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/JetBrainsMono.zip
    unzip JetBrainsMono.zip -d ~/.local/share/fonts
    rm JetBrainsMono.zip
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
