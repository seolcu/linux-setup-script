#!/usr/bin/env bash

echo -n "Install Rustup? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
fi

echo -n "Install Proton-GE with asdf? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.0
    echo -e '\n. "$HOME/.asdf/asdf.sh"' >> ~/.bashrc
    echo '. "$HOME/.asdf/completions/asdf.bash"' >> ~/.bashrc
    source ~/.bashrc
    asdf plugin add protonge
    asdf install protonge latest
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

echo -n "Add nord colorscheme to Konsole? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    mkdir -p ~/.local/share/konsole
    curl -o ~/.local/share/konsole/Nord.colorscheme https://raw.githubusercontent.com/nordtheme/konsole/develop/src/nord.colorscheme
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