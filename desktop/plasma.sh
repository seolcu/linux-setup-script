#!/usr/bin/env bash

echo -n "Setup Fcitx5 environment variable for XWayland? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    echo 'XMODIFIERS=@im=fcitx' | sudo tee -a /etc/environment
fi