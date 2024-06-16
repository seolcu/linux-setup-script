#!/usr/bin/env bash

echo -n "Setup Fcitx5 environment variable for XWayland? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo 'XMODIFIERS=@im=fcitx' | sudo tee -a /etc/environment
fi

echo -n "Apply Wayland & Wayland native input method flag for brave & vscode? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    cp config/flags/* ~/.config/
fi