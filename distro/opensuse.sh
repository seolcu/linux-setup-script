#!/usr/bin/bash

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

echo -n "Install VSCode? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
    echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ntype=rpm-md\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" |sudo tee /etc/zypp/repos.d/vscode.repo > /dev/null
    sudo zypper refresh
    sudo zypper install code
fi

echo -n "Change hostname? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo -n "Enter new hostname: "
    read hostname
    sudo hostnamectl set-hostname "$hostname"
fi

echo -n "Setup virtualization with Yast? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo yast2 virtualization
    sudo usermod -a -G libvirt $(whoami)
    sudo virsh net-autostart default
fi