# change to debian sid
sudo mv /etc/apt/sources.list /etc/apt/sources.list.old
sudo cat > /etc/apt/sources.list<<EOF
deb http://deb.debian.org/debian unstable main non-free-firmware contrib non-free
deb-src http://deb.debian.org/debian unstable main non-free-firmware contrib non-free
EOF
sudo apt update
sudo apt full-upgrade -y


# install essential packages
sudo apt install git gcc g++ curl flatpak gnome-software-plugin-flatpak htop neofetch python3-nautilus


# install vscode
curl -o vscode.deb https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64
sudo apt install ./vscode.deb


# debloat
sudo apt remove gnome-games rhythmbox evolution zutty transmission-common shotwell
sudo apt autoremove


# install flatpak packages
flatpak install flathub com.spotify.Client
flatpak install flathub org.videolan.VLC
flatpak install flathub com.microsoft.Edge
flatpak install flathub com.github.tchx84.Flatseal
flatpak install flathub com.mattjakeman.ExtensionManager
flatpak install flathub com.usebottles.bottles
flatpak install flathub us.zoom.Zoom
flatpak install flathub com.github.unrud.VideoDownloader
flatpak install flathub com.protonvpn.www
flatpak install flathub md.obsidian.Obsidian
flatpak install flathub org.gnome.Boxes
flatpak install flathub org.remmina.Remmina
flatpak install flathub org.gnome.NetworkDisplays
flatpak install flathub com.rafaelmardojai.Blanket
flatpak install flathub in.srev.guiscrcpy
flatpak install flathub org.gabmus.whatip


# [Enable Function Keys On Keychron/Various Mechanical Keyboards Under Linux, with systemd](https://github.com/adam-savard/keyboard-function-keys-linux)
sudo cat > /etc/systemd/system/keychron.service<<EOF
[Unit]
Description=Disable media keys and substitute in function keys

[Service]
Type=simple
RemainAfterExit=yes
ExecStart=/bin/bash -c "echo 0 > /sys/module/hid_apple/parameters/fnmode"
ExecStop=/bin/bash -c "echo 1 > /sys/module/hid_apple/parameters/fnmode"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl enable keychron
sudo systemctl start keychron

