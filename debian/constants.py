# Constants

APT_PACKAGES: list[str] = [
    # GUI
    "chromium",
    "solaar",
    "virt-manager",
    # CLI
    ## Development
    ### C/C++
    "gcc",
    "g++",
    ### Java
    "default-jdk",
    ### Python
    "python3-pip",
    "python3-venv",
    "python3-ipykernel",
    "black",
    ### Node.js
    "nodejs",
    ## Utilities
    "curl",
    "wget",
    "htop",
    "neofetch",
    "git",
    "gh",
    "distrobox",
    # Plugins
    ## GNOME extensions
    "gnome-shell-extension-appindicator",
    "gnome-shell-extension-caffeine",
    "gnome-shell-extension-gamemode",
    "gnome-shell-extension-gsconnect",
    ## Flatpak
    "flatpak",
    "gnome-software-plugin-flatpak",
    ## Etc
    "hugo",
]

MANUAL_PACKAGES: list[dict[str, str]] = [
    {
        "name": "Visual Studio Code",
        "install": """
sudo apt-get install wget gpg -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt install apt-transport-https -y
sudo apt update -y
sudo apt install code -y
""",
    },
    {
        "name": "NeoVIM(AppImage)",
        "install": """
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage
sudo mv nvim.appimage /usr/local/bin/nvim
sudo chmod +x /usr/local/bin/nvim
CUSTOM_NVIM_PATH=/usr/local/bin/nvim
set -u
sudo update-alternatives --install /usr/bin/ex ex "${CUSTOM_NVIM_PATH}" 110
sudo update-alternatives --install /usr/bin/vi vi "${CUSTOM_NVIM_PATH}" 110
sudo update-alternatives --install /usr/bin/view view "${CUSTOM_NVIM_PATH}" 110
sudo update-alternatives --install /usr/bin/vim vim "${CUSTOM_NVIM_PATH}" 110
sudo update-alternatives --install /usr/bin/vimdiff vimdiff "${CUSTOM_NVIM_PATH}" 110
""",
    },
    {
        "name": "ProtonVPN",
        "install": """
wget -P . -O protonvpn.deb https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3-2_all.deb
sudo apt install -f -y ./protonvpn.deb
rm ./protonvpn.deb
sudo apt update -y
sudo apt install -y proton-vpn-gnome-desktop
""",
    },
]

FLATPAK_PACKAGES: list[str] = [
    # GNOME Apps
    ## Etc
    "com.belmoussaoui.Decoder",
    "com.usebottles.bottles",
    # Work
    "org.onlyoffice.desktopeditors",
    "md.obsidian.Obsidian",
    # Utilities
    "org.raspberrypi.rpi-imager",
    # Games
    "com.valvesoftware.Steam",
    # Etc
    "com.obsproject.Studio",
]
