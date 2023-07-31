from subprocess import run
from simple_term_menu import TerminalMenu


class package:
    def __init__(self, name: str):
        self.name: str = name


class manual_package(package):
    def __init__(
        self,
        name: str,
        install_command: str,
        remove_command: str,
    ):
        super().__init__(name)
        self.install_command: str = install_command
        self.remove_command: str = remove_command


class flathub_package(package):
    def __init__(self, name: str):
        super().__init__(name)


class apt_package(package):
    def __init__(self, name: str):
        super().__init__(name)


class gnome_extension_package(package):
    def __init__(self, name: str):
        super().__init__(name)


class package_list:
    def register(self):
        self.registered_indexes: tuple[int] | None = TerminalMenu(
            map(lambda a_package: a_package.name, self.raw_package_list),
            multi_select=True,
            show_multi_select_hint=True,
            multi_select_select_on_accept=False,
            multi_select_empty_ok=True,
        ).show()

    def isRegistered(self):
        if str(type(self.registered_indexes)) == "<class 'tuple'>":
            return True
        else:
            print("Nothing is registered")
            return False

    def __init__(self, raw_package_list: list[package]):
        self.raw_package_list: list[package] = raw_package_list


class manual_package_list(package_list):
    def install(self):
        if self.isRegistered():
            for index in self.registered_indexes:
                run(self.raw_package_list[index].install_command, shell=True)

    def __init__(self, raw_package_list: list[manual_package]):
        self.raw_package_list: list[manual_package] = raw_package_list


class flathub_package_list(package_list):
    def install(self):
        if self.isRegistered():
            install_str = "flatpak install -y flathub"
            for index in self.registered_indexes:
                install_str += " " + self.raw_package_list[index].name
            run(install_str, shell=True)

    def __init__(self, raw_package_list: list[flathub_package]):
        self.raw_package_list: list[flathub_package] = raw_package_list


class apt_package_list(package_list):
    def install(self):
        if self.isRegistered():
            install_str = "sudo apt install -y"
            for index in self.registered_indexes:
                install_str += " " + self.raw_package_list[index].name
            run(install_str, shell=True)

    def remove(self):
        if self.isRegistered():
            remove_str = "sudo apt remove -y"
            for index in self.registered_indexes:
                remove_str += " " + self.raw_package_list[index].name
            run(remove_str, shell=True)

    def __init__(self, raw_package_list: list[apt_package]):
        self.raw_package_list: list[apt_package] = raw_package_list


class gnome_extension_package_list(package_list):
    def install(self):
        if self.isRegistered():
            install_str = "gext install"
            for index in self.registered_indexes:
                install_str += " " + self.raw_package_list[index].name
            run(install_str, shell=True)

    def __init__(self, raw_package_list: list[gnome_extension_package]):
        self.raw_package_list: list[gnome_extension_package] = raw_package_list


manual_install_packages: manual_package_list = manual_package_list(
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
    ]
)

flathub_install_packages: flathub_package_list = flathub_package_list(
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
)

apt_install_packages: apt_package_list = apt_package_list(
    [
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
)

gnome_extension_install_packages: gnome_extension_package_list = (
    gnome_extension_package_list(
        [
            gnome_extension_package("appindicatorsupport@rgcjonas.gmail.com"),
            gnome_extension_package("caffeine@patapon.info"),
            gnome_extension_package("gsconnect@andyholmes.github.io"),
            gnome_extension_package("gestureImprovements@gestures"),
            gnome_extension_package("Vitals@CoreCoding.com"),
        ]
    )
)

apt_remove_packages: apt_package_list = apt_package_list(
    [
        apt_package("gnome-games"),
        apt_package("rhythmbox"),
        apt_package("evolution"),
        apt_package("zutty"),
        apt_package("shotwell"),
    ]
)
