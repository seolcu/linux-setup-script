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