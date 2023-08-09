import helpers as h

DISTRO_LIST: list[str] = ["debian", "fedora"]
DE_LIST: list[str] = ["gnome"]


DISTRO_PACKAGES: dict[str, dict[str, h.package_list]] = {
    "common": {
        "install": h.package_list(
            [
                h.flathub_package("in.srev.guiscrcpy"),
                h.flathub_package("org.gnome.Boxes"),
                h.flathub_package("com.mojang.Minecraft"),
                h.flathub_package("io.mrarm.mcpelauncher"),
                h.flathub_package("com.valvesoftware.Steam"),
                h.flathub_package("com.rafaelmardojai.Blanket"),
                h.flathub_package("org.gnome.NetworkDisplays"),
                h.flathub_package("com.obsproject.Studio"),
                h.flathub_package("org.videolan.VLC"),
                h.flathub_package("md.obsidian.Obsidian"),
                h.flathub_package("org.onlyoffice.desktopeditors"),
                h.flathub_package("com.usebottles.bottles"),
                h.flathub_package("de.haeckerfelix.Fragments"),
                h.flathub_package("com.discordapp.Discord"),
                h.flathub_package("com.github.ztefn.haguichi"),
                h.flathub_package("com.microsoft.Edge"),
                h.flathub_package("org.gabmus.whatip"),
                h.flathub_package("us.zoom.Zoom"),
                h.flathub_package("com.github.unrud.VideoDownloader"),
                h.flathub_package("com.github.tchx84.Flatseal"),
                h.flathub_package("com.mattjakeman.ExtensionManager"),
                h.flathub_package("com.spotify.Client"),
                h.flathub_package("com.protonvpn.www"),
                h.flathub_package("org.remmina.Remmina"),
            ]
        ),
        "remove": h.package_list([]),
    },
    "debian": {
        "install": h.package_list(
            [
                h.manual_package(
                    "vscode-apt",
                    """
                sudo apt install -y wget gpg
                wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
                sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
                sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
                rm -f packages.microsoft.gpg
                sudo apt install apt-transport-https
                sudo apt update -y
                sudo apt install -y code
            """,
                    "sudo apt remove -y code",
                ),
                h.apt_package("gnome-software-plugin-flatpak"),
                h.apt_package("git"),
                h.apt_package("gcc"),
                h.apt_package("g++"),
                h.apt_package("curl"),
                h.apt_package("wget"),
                h.apt_package("gpg"),
                h.apt_package("htop"),
                h.apt_package("neofetch"),
                h.apt_package("gh"),
                h.apt_package("solaar"),
                h.apt_package("python3-nautilus"),
            ]
        ),
        "remove": h.package_list(
            [
                h.apt_package("gnome-games"),
                h.apt_package("rhythmbox"),
                h.apt_package("evolution"),
                h.apt_package("zutty"),
                h.apt_package("shotwell"),
            ]
        ),
    },
    "fedora": {"install": h.package_list([]), "remove": h.package_list([])},
}

DE_PACKAGES: dict[str, dict[str, h.package_list]] = {
    "gnome": {
        "install": h.package_list(
            [
                h.gnome_extension_package("appindicatorsupport@rgcjonas.gmail.com"),
                h.gnome_extension_package("caffeine@patapon.info"),
                h.gnome_extension_package("gsconnect@andyholmes.github.io"),
                h.gnome_extension_package("gestureImprovements@gestures"),
                h.gnome_extension_package("Vitals@CoreCoding.com"),
            ]
        ),
        "remove": h.package_list([]),
    }
}

DISTRO_SCRIPTS = {
    "common": {
        "before": h.bash_script_list(
            [
                h.bash_script(
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
        "after": h.bash_script_list(
            [
                h.bash_script(
                    "Reboot",
                    """
                        sudo systemctl reboot
                    """,
                    ask=True,
                )
            ]
        ),
    },
    "debian": {
        "before": h.bash_script_list(
            [
                h.bash_script(
                    "Switching to Debian sid",
                    """
                        sudo mv /etc/apt/sources.list /etc/apt/sources.list.old
                        sudo cp ./assets/sources.list /etc/apt/sources.list
                    """,
                    ask=True,
                ),
                h.bash_script(
                    "Updating the system",
                    """
                        sudo apt update -y
                        sudo apt full-upgrade -y
                    """,
                ),
                h.bash_script(
                    "Setting up flatpak & flathub",
                    """
                        sudo apt install -y flatpak
                        sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
                    """,
                ),
            ]
        ),
        "after": h.bash_script_list(
            [
                h.bash_script(
                    "Removing packages",
                    """
                        sudo apt autoremove -y
                    """,
                )
            ]
        ),
    },
    "fedora": {
        "before": h.bash_script_list(
            [
                h.bash_script(
                    "Updating the system",
                    """
                        sudo dnf update -y
                    """,
                ),
                h.bash_script(
                    "Enabling RPM Fusion",
                    """
                        sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
                        sudo dnf groupupdate -y core
                    """,
                ),
                h.bash_script(
                    "Installing codecs from RPM Fusion",
                    """
                        sudo dnf swap -y ffmpeg-free ffmpeg --allowerasing
                        sudo dnf groupupdate -y multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
                        sudo dnf groupupdate -y sound-and-video
                        sudo dnf swap -y mesa-va-drivers mesa-va-drivers-freeworld
                        sudo dnf swap -y mesa-vdpau-drivers mesa-vdpau-drivers-freeworld
                        sudo dnf swap -y mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686
                        sudo dnf swap -y mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686
                    """,
                ),
            ]
        ),
        "after": h.bash_script_list([]),
    },
}
