from helpers import (
    package_list,
    manual_package,
    flathub_package,
    apt_package,
    gnome_extension_package,
    bash_script,
    bash_script_list,
)

DISTRO_LIST: list[str] = ["debian", "fedora"]
DE_LIST: list[str] = ["gnome", "kde"]


DISTRO_PACKAGES: dict[str, dict[str, package_list]] = {
    "common": {
        "install": package_list(
            [
                flathub_package("in.srev.guiscrcpy"),
                flathub_package("org.gnome.Boxes"),
                flathub_package("com.mojang.Minecraft"),
                flathub_package("io.mrarm.mcpelauncher"),
                flathub_package("com.valvesoftware.Steam"),
                flathub_package("com.rafaelmardojai.Blanket"),
                flathub_package("org.gnome.NetworkDisplays"),
                flathub_package("com.obsproject.Studio"),
                flathub_package("org.videolan.VLC"),
                flathub_package("md.obsidian.Obsidian"),
                flathub_package("org.onlyoffice.desktopeditors"),
                flathub_package("com.usebottles.bottles"),
                flathub_package("de.haeckerfelix.Fragments"),
                flathub_package("com.discordapp.Discord"),
                flathub_package("com.github.ztefn.haguichi"),
                flathub_package("com.microsoft.Edge"),
                flathub_package("org.gabmus.whatip"),
                flathub_package("us.zoom.Zoom"),
                flathub_package("com.github.unrud.VideoDownloader"),
                flathub_package("com.github.tchx84.Flatseal"),
                flathub_package("com.mattjakeman.ExtensionManager"),
                flathub_package("com.spotify.Client"),
                flathub_package("com.protonvpn.www"),
                flathub_package("org.remmina.Remmina"),
            ]
        ),
        "remove": package_list([]),
    },
    "debian": {
        "install": package_list(
            [
                manual_package(
                    "vscode-apt",
                    """
                sudo apt install wget gpg
                wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
                sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
                sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
                rm -f packages.microsoft.gpg
                sudo apt install apt-transport-https
                sudo apt update
                sudo apt install code
            """,
                    "sudo apt remove -y code",
                ),
                apt_package("gnome-software-plugin-flatpak"),
                apt_package("git"),
                apt_package("gcc"),
                apt_package("g++"),
                apt_package("curl"),
                apt_package("wget"),
                apt_package("gpg"),
                apt_package("htop"),
                apt_package("neofetch"),
                apt_package("gh"),
                apt_package("solaar"),
                apt_package("python3-nautilus"),
            ]
        ),
        "remove": package_list(
            [
                apt_package("gnome-games"),
                apt_package("rhythmbox"),
                apt_package("evolution"),
                apt_package("zutty"),
                apt_package("shotwell"),
            ]
        ),
    },
    "fedora": {"install": package_list([]), "remove": package_list([])},
}

DE_PACKAGES: dict[str, dict[str, package_list]] = {
    "gnome": {
        "install": package_list(
            [
                gnome_extension_package("appindicatorsupport@rgcjonas.gmail.com"),
                gnome_extension_package("caffeine@patapon.info"),
                gnome_extension_package("gsconnect@andyholmes.github.io"),
                gnome_extension_package("gestureImprovements@gestures"),
                gnome_extension_package("Vitals@CoreCoding.com"),
            ]
        ),
        "remove": package_list([]),
    }
}

DISTRO_SCRIPTS = {
    "common": {
        "before": bash_script_list(
            [
                bash_script(
                    # [Enable Function Keys On Keychron/Various Mechanical Keyboards Under Linux, with systemd](https://github.com/adam-savard/keyboard-function-keys-linux)
                    "Fixing keyboard Fn issue (https://github.com/adam-savard/keyboard-function-keys-linux)",
                    """
                        sudo cp ./assets/keychron.service /etc/systemd/system/keychron.service
                        sudo systemctl enable keychron
                        sudo systemctl start keychron
                    """,
                    ask=True,
                )
            ]
        ),
        "after": bash_script_list([]),
    },
    "debian": {
        "before": bash_script_list(
            [
                bash_script(
                    "Switching to Debian sid",
                    """
                        sudo mv /etc/apt/sources.list /etc/apt/sources.list.old
                        sudo cp ./assets/sources.list /etc/apt/sources.list
                    """,
                    ask=True,
                ),
                bash_script(
                    "Updating the system",
                    """
                        sudo apt update
                        sudo apt full-upgrade -y
                    """,
                ),
                bash_script(
                    "Setting up flatpak & flathub",
                    """
                        sudo apt install -y flatpak
                        sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
                    """,
                ),
            ]
        ),
        "after": bash_script_list(
            [
                bash_script(
                    "Removing packages",
                    """
                        sudo apt autoremove -y
                    """,
                )
            ]
        ),
    },
    "fedora": {"before": bash_script_list([]), "after": bash_script_list([])},
}
