#!/usr/bin/env bash

echo -n "Setup Fcitx5 environment variables? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo 'GTK_IM_MODULE=fcitx' | sudo tee -a /etc/environment
    echo 'QT_IM_MODULE=fcitx' | sudo tee -a /etc/environment
    echo 'XMODIFIERS=@im=fcitx' | sudo tee -a /etc/environment
fi

echo -n "Add nord colorscheme to Konsole? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    mkdir -p ~/.local/share/konsole
    curl -o ~/.local/share/konsole/Nord.colorscheme https://raw.githubusercontent.com/nordtheme/konsole/develop/src/nord.colorscheme
fi