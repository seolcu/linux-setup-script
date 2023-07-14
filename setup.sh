# change to debian sid
mv /etc/apt/sources.list /etc/apt/sources.list.old
cat > /etc/apt/sources.list<<EOF
deb http://deb.debian.org/debian unstable main non-free-firmware contrib non-free
deb-src http://deb.debian.org/debian unstable main non-free-firmware contrib non-free
EOF
apt update
apt full-upgrade -y


# install essential packages
apt install -y git gcc g++ curl wget gpg htop neofetch solaar python3-nautilus


# install vscode
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
apt install -y apt-transport-https
apt update
apt install -y code


# debloat
apt remove -y gnome-games rhythmbox evolution zutty transmission-common shotwell
apt autoremove -y


# setup flatpak
apt install -y flatpak gnome-software-plugin-flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo


# install flatpak packages
flatpak install flathub -y com.spotify.Client org.videolan.VLC com.microsoft.Edge com.github.tchx84.Flatseal com.mattjakeman.ExtensionManager com.usebottles.bottles us.zoom.Zoom com.github.unrud.VideoDownloader com.protonvpn.www md.obsidian.Obsidian org.gnome.Boxes org.remmina.Remmina org.gnome.NetworkDisplays com.rafaelmardojai.Blanket in.srev.guiscrcpy org.gabmus.whatip


# [Enable Function Keys On Keychron/Various Mechanical Keyboards Under Linux, with systemd](https://github.com/adam-savard/keyboard-function-keys-linux)
cat > /etc/systemd/system/keychron.service<<EOF
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
systemctl enable keychron
systemctl start keychron
