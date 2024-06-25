#!/usr/bin/env bash

# Packages

echo -n "Install Rustup? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
fi

# Configuration

echo -n "Setup virt-manager for KVM? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo systemctl enable --now libvirtd
    sudo usermod -a -G libvirt $(whoami)
    sudo virsh net-autostart default
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

echo -n "Load fastfetch configuration? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    mkdir -p ~/.config/fastfetch
    curl -o ~/.config/fastfetch/config.jsonc https://raw.githubusercontent.com/fastfetch-cli/fastfetch/dev/presets/examples/10.jsonc
fi

echo -n "Add simplified fastfetch to .bashrc? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    mkdir -p ~/.config/fastfetch/presets
    curl -o ~/.config/fastfetch/presets/9.jsonc https://raw.githubusercontent.com/fastfetch-cli/fastfetch/dev/presets/examples/9.jsonc
    echo -e "\nfastfetch -c ~/.config/fastfetch/presets/9.jsonc" >> ~/.bashrc
fi

echo -n "Add starship init to .bashrc? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo -e '\neval "$(starship init bash)"' >> ~/.bashrc
fi

echo -n "Apply Wayland & Wayland native input method flag for Brave (Native)? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    cp config/flags/electron-flags.conf ~/.config/brave-flags.conf
fi

echo -n "Apply Wayland & Wayland native input method flag for Brave (Flatpak)? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    cp config/flags/electron-flags.conf ~/.var/app/com.brave.Browser/config/brave-flags.conf
fi

echo -n "Apply Wayland & Wayland native input method flag for vscode? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    cp config/flags/electron-flags.conf ~/.config/code-flags.conf
fi