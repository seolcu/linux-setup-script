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
        selected_indexes: int | tuple[int] | None = TerminalMenu(
            map(lambda a_package: a_package.name, self.raw_package_list),
            multi_select=True,
            show_multi_select_hint=True,
            multi_select_select_on_accept=False,
            multi_select_empty_ok=True,
        ).show()
        if type(selected_indexes) == int:
            self.registered_indexes: tuple[int] = (selected_indexes,)
        elif type(selected_indexes) == tuple[int]:
            self.registered_indexes: tuple[int] = selected_indexes

    def __init__(self, raw_package_list: list[package]):
        self.raw_package_list: list[package] = raw_package_list


class manual_package_list(package_list):
    def install(self):
        if type(self.registered_indexes) == int:
            run(
                self.raw_package_list[self.registered_indexes].install_command,
                shell=True,
            )
        elif type(self.registered_indexes) == tuple[int]:
            for index in self.registered_indexes:
                run(self.raw_package_list[index].install_command, shell=True)

    def __init__(self, raw_package_list: list[manual_package]):
        self.raw_package_list: list[manual_package] = raw_package_list


class flathub_package_list(package_list):
    def install(self):
        install_str = "flatpak install -y flathub"
        for index in self.registered_indexes:
            install_str += " " + self.raw_package_list[index].name
        run(install_str, shell=True)

    def __init__(self, raw_package_list: list[flathub_package]):
        self.raw_package_list: list[flathub_package] = raw_package_list


class apt_package_list(package_list):
    def install(self):
        install_str = "sudo apt install -y"
        for index in self.registered_indexes:
            install_str += " " + self.raw_package_list[index].name
        run(install_str, shell=True)

    def remove(self):
        remove_str = "sudo apt remove -y"
        for index in self.registered_indexes:
            remove_str += " " + self.raw_package_list[index].name
        run(remove_str, shell=True)

    def __init__(self, raw_package_list: list[apt_package]):
        self.raw_package_list: list[apt_package] = raw_package_list


class gnome_extension_package_list(package_list):
    def install(self):
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


from colorama import Fore, Style
from simple_term_menu import TerminalMenu
from subprocess import run


def display_title(title: str):
    print(Fore.GREEN + f"[!] {title}", end=f"{Style.RESET_ALL}\n")


class linux:
    def fix_keyboard(self):
        # [Enable Function Keys On Keychron/Various Mechanical Keyboards Under Linux, with systemd](https://github.com/adam-savard/keyboard-function-keys-linux)
        display_title(
            "Fix keyboard Fn keys issue? (https://github.com/adam-savard/keyboard-function-keys-linux)"
        )
        if TerminalMenu(["No", "Yes"]).show():
            run(
                """
                    sudo cp ./assets/keychron.service /etc/systemd/system/keychron.service
                    sudo systemctl enable keychron
                    sudo systemctl start keychron
                """,
                shell=True,
            )

    def configure(self):
        display_title("Select manual packages to install")
        manual_install_packages.register()
        display_title("Select flathub packages to install")
        flathub_install_packages.register()
        if self.DE == "gnome":
            display_title("Select gnome extensions to install")
            gnome_extension_install_packages.register()

    def proceed(self):
        display_title("Installing packages")
        manual_install_packages.install()
        flathub_install_packages.install()
        apt_install_packages.install()
        gnome_extension_install_packages.install()

        display_title("Removing packages")
        apt_remove_packages.remove()
        run("sudo apt autoremove -y", shell=True)

    def __init__(self, DE: str):
        # DE: "gnome", "kde", "xfce", ...
        self.DE: str = DE


class debian(linux):
    def switch_to_debian_sid():
        display_title("Switch to Debian sid?")
        if TerminalMenu(["No", "Yes"]).show():
            run(
                """
                    sudo mv /etc/apt/sources.list /etc/apt/sources.list.old
                    sudo cp ./assets/sources.list /etc/apt/sources.list
                """,
                shell=True,
            )

    def apt_update():
        display_title("Updating the system")
        run(
            """
                sudo apt update
                sudo apt full-upgrade -y
            """,
            shell=True,
        )

    def apt_setup_flatpak():
        display_title("Setting up flatpak & flathub")
        run(
            """
                sudo apt install -y flatpak
                sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
            """,
            shell=True,
        )

    def configure(self):
        super().configure()
        display_title("Select apt packages to install")
        apt_install_packages.register()
        display_title("Select apt packages to remove")
        apt_remove_packages.register()

    def __init__(self, DE: str):
        super().__init__(DE)


def register_all():
    display_title("Select manual packages to install")
    manual_install_packages.register()

    display_title("Select flathub packages to install")
    flathub_install_packages.register()

    display_title("Select apt packages to install")
    apt_install_packages.register()

    display_title("Select gnome extensions to install")
    gnome_extension_install_packages.register()

    display_title("Select apt packages to remove")
    apt_remove_packages.register()


def proceed_all():
    display_title("Installing packages")
    manual_install_packages.install()
    flathub_install_packages.install()
    apt_install_packages.install()
    gnome_extension_install_packages.install()

    display_title("Removing packages")
    apt_remove_packages.remove()
    run("sudo apt autoremove -y", shell=True)
