from colorama import Fore, Style
from subprocess import run
from simple_term_menu import TerminalMenu
import constants as c


# Classes


class Package:
    name: str
    install_command: str
    remove_command: str

    # is_install: 0 is remove, 1 is install
    def __process__(self, is_install: bool) -> None:
        if is_install:
            bash(self.install_command)
        else:
            bash(self.remove_command)

    def install(self) -> None:
        self.__process__(True)

    def remove(self) -> None:
        self.__process__(False)


class ManualPackage(Package):
    def __init__(
        self,
        name: str,
        install_command: str,
        remove_command: str,
    ) -> None:
        self.name: str = f"manual: {name}"
        self.install_command: str = install_command
        self.remove_command: str = remove_command


class FlatpakPackage(Package):
    def __init__(self, url: str) -> None:
        self.url: str = url
        self.name: str = f"flatpak: {url}"
        self.install_command: str = f"flatpak install -y {url}"
        self.remove_command: str = f"flatpak remove -y {url}"


class AptPackage(Package):
    def __init__(self, apt_name: str) -> None:
        self.apt_name: str = apt_name
        self.name: str = f"apt: {apt_name}"
        self.install_command: str = f"sudo apt install -y {apt_name}"
        self.remove_command: str = f"sudo apt autoremove -y {apt_name}"


class GnomeExtensionPackage(Package):
    def __init__(self, url: str) -> None:
        self.url: str = url
        self.name: str = f"GNOME Extension: {url}"
        self.install_command: str = f"gext install {url}"
        self.remove_command: str = f"gext uninstall {url}"


class PackageList:
    def __register__(self, is_install: bool = True) -> int | tuple[int, ...] | None:
        if len(self.raw_package_list) != 0:
            display_question(
                f"Select packages to {'install' if is_install else 'remove'}"
            )

            registered_indexes: int | tuple[int, ...] | None = TerminalMenu(
                map(lambda a_package: a_package.name, self.raw_package_list),
                multi_select=True,
                show_multi_select_hint=True,
                multi_select_select_on_accept=False,
                multi_select_empty_ok=True,
            ).show()
            return registered_indexes
        else:
            display_warning("No packages registered")
            return None

    def __process__(
        self, is_install: bool = True, indexes: int | tuple[int, ...] | None = None
    ) -> None:
        if type(indexes) == None:
            display_warning("No packages registered")
        elif type(indexes) == int:
            index = indexes
            self.raw_package_list[index].__process__(is_install)
        elif type(indexes) == tuple:
            for index in indexes:
                self.raw_package_list[index].__process__(is_install)

    def __register_and_process__(self, is_install: bool = True) -> None:
        self.__process__(is_install, self.__register__(is_install))

    def register_and_install(self) -> None:
        self.__register_and_process__(is_install=True)

    def register_and_remove(self) -> None:
        self.__register_and_process__(is_install=False)

    def __init__(self, raw_package_list: list[Package]) -> None:
        self.raw_package_list: list[Package] = raw_package_list


class BashScript:
    def __ask__(self) -> bool:
        display_question(self.question)
        return no_or_yes()

    def __execute__(self) -> None:
        bash(self.command)

    def ask_and_execute(self) -> None:
        if self.__ask__():
            self.__execute__()

    def __init__(self, question: str, command: str) -> None:
        self.question: str = question
        self.command: str = command


# Functions


def display_title(title: str) -> None:
    print(Fore.GREEN + f"[!] {title}", end=f"{Style.RESET_ALL}\n")


def display_question(question: str) -> None:
    print(Fore.BLUE + question, end=f"{Style.RESET_ALL}\n")


def display_warning(warning: str) -> None:
    print(Fore.YELLOW + warning, end=f"{Style.RESET_ALL}\n")


def no_or_yes() -> bool:
    ans: int | tuple[int, ...] | None = TerminalMenu(["No", "Yes"]).show()
    if type(ans) == int:
        return bool(ans)
    else:
        display_warning("No option selected")
        return no_or_yes()


def select_one(options: list[str]) -> int:
    index: int | tuple[int, ...] | None = TerminalMenu(options).show()
    if type(index) == int:
        return index
    else:
        display_warning("No option selected")
        return select_one(options)


def bash(command: str) -> None:
    run(command, shell=True)


# Instances

distro_packages: dict[str, dict[str, PackageList]] = {
    "common": {
        "install": PackageList(
            [
                # GNOME Apps
                ## Core
                FlatpakPackage("org.gnome.Snapshot"),
                FlatpakPackage("org.gnome.Connections"),
                FlatpakPackage("org.gnome.Extensions"),
                FlatpakPackage("org.gnome.Loupe"),
                FlatpakPackage("org.gnome.Music"),
                ## Circle
                FlatpakPackage("com.rafaelmardojai.Blanket"),
                FlatpakPackage("org.gnome.design.Emblem"),
                FlatpakPackage("de.haeckerfelix.Fragments"),
                FlatpakPackage("io.gitlab.adhami3310.Impression"),
                FlatpakPackage("io.gitlab.gregorni.Letterpress"),
                FlatpakPackage("com.belmoussaoui.Obfuscate"),
                FlatpakPackage("org.gnome.Solanum"),
                FlatpakPackage("org.gnome.gitlab.YaLTeR.VideoTrimmer"),
                FlatpakPackage("re.sonny.Workbench"),
                ## Development
                FlatpakPackage("org.gnome.Boxes"),
                FlatpakPackage("org.gnome.Builder"),
                ## Etc
                FlatpakPackage("com.usebottles.bottles"),
                FlatpakPackage("org.gnome.NetworkDisplays"),
                FlatpakPackage("org.gabmus.whatip"),
                FlatpakPackage("org.gimp.GIMP"),
                ManualPackage(
                    "Firefox Gnome Theme",
                    "curl -s -o- https://raw.githubusercontent.com/rafaelmardojai/firefox-gnome-theme/master/scripts/install-by-curl.sh | bash",
                    "",
                ),
                # KDE Apps
                FlatpakPackage("org.kde.kdenlive"),
                # Work
                FlatpakPackage("org.onlyoffice.desktopeditors"),
                FlatpakPackage("md.obsidian.Obsidian"),
                # Communication
                FlatpakPackage("us.zoom.Zoom"),
                FlatpakPackage("im.riot.Riot"),
                # Utilities
                FlatpakPackage("com.github.tchx84.Flatseal"),
                FlatpakPackage("com.obsproject.Studio"),
                FlatpakPackage("com.github.unrud.VideoDownloader"),
                FlatpakPackage("org.raspberrypi.rpi-imager"),
                # Web
                FlatpakPackage("com.microsoft.Edge"),
                FlatpakPackage("com.protonvpn.www"),
                # Games
                FlatpakPackage("com.valvesoftware.Steam"),
                FlatpakPackage("com.discordapp.Discord"),
                FlatpakPackage("com.mojang.Minecraft"),
                FlatpakPackage("io.mrarm.mcpelauncher"),
                FlatpakPackage("com.github.ztefn.haguichi"),
                FlatpakPackage("com.adobe.Flash-Player-Projector"),
                # Etc
                FlatpakPackage("com.spotify.Client"),
                FlatpakPackage("in.srev.guiscrcpy"),
                FlatpakPackage("org.remmina.Remmina"),
                FlatpakPackage("org.videolan.VLC"),
            ]
        ),
    },
    "debian": {
        "install": PackageList(
            [
                # GUI
                ## Development
                ManualPackage(
                    "vscode",
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
                ManualPackage(
                    "virt-manager",
                    """
                        sudo apt install -y virt-manager
                        sudo usermod -a -G libvirt $(whoami)
                        sudo virsh net-autostart default
                        sudo virsh net-start default
                    """,
                    "sudo apt remove -y virt-manager",
                ),
                AptPackage("gnome-boxes"),
                AptPackage("gnome-console"),
                ## Etc
                AptPackage("timeshift"),
                AptPackage("solaar"),
                ManualPackage(
                    "ProtonVPN",
                    """
                        wget -P . -O protonvpn.deb https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3-2_all.deb
                        sudo apt install -f -y ./protonvpn.deb
                        rm ./protonvpn.deb
                        sudo apt update -y
                        sudo apt install -y protonvpn
                    """,
                    "sudo apt remove protonvpn",
                ),
                # CLI
                ## Development
                ### C/C++
                AptPackage("gcc"),
                AptPackage("g++"),
                ### Java
                AptPackage("default-jdk"),
                ### Python
                AptPackage("python3-pip"),
                AptPackage("python3-venv"),
                AptPackage("python3-ipykernel"),
                AptPackage("black"),
                ### Node.js
                ManualPackage(
                    "nvm",
                    """
                        sudo apt install -y curl
                        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
                    """,
                    "",
                ),
                ### Ruby
                AptPackage("ruby-full"),
                AptPackage("bundler"),
                AptPackage("jekyll"),
                ## Utilities
                AptPackage("curl"),
                AptPackage("wget"),
                AptPackage("gpg"),
                AptPackage("htop"),
                AptPackage("neofetch"),
                AptPackage("gh"),
                AptPackage("distrobox"),
                # Plugins
                ## GNOME extensions
                AptPackage("gnome-shell-extension-appindicator"),
                AptPackage("gnome-shell-extension-caffeine"),
                AptPackage("gnome-shell-extension-gamemode"),
                AptPackage("gnome-shell-extension-gsconnect"),
                ## Etc
                AptPackage("gnome-software-plugin-flatpak"),
                AptPackage("python3-nautilus"),
                AptPackage("steam-devices"),
            ]
        ),
        "remove": PackageList(
            [
                # [!] Don't remove gnome-terminal
                # Mess
                AptPackage("gnome-games"),
                AptPackage("rhythmbox"),
                AptPackage("evolution"),
                AptPackage("zutty"),
                AptPackage("shotwell"),
                # Replace to newer apps
                AptPackage("transmission-*"),
                AptPackage("cheese"),
                AptPackage("eog"),
            ]
        ),
    },
}


de_packages: dict[str, dict[str, PackageList]] = {
    "gnome": {
        "install": PackageList(
            [
                GnomeExtensionPackage("gestureImprovements@gestures"),
                GnomeExtensionPackage("Vitals@CoreCoding.com"),
                GnomeExtensionPackage("thinkpad-battery-threshold@marcosdalvarez.org"),
                FlatpakPackage("com.mattjakeman.ExtensionManager"),
                FlatpakPackage("io.github.realmazharhussain.GdmSettings"),
            ]
        ),
    }
}


# Main


def main():
    # 0. prepare

    display_title("Welcome to the Linux Setup Script")

    display_question("Select your distro")
    distro = c.DISTRO_LIST[select_one(c.DISTRO_LIST)]
    display_question("Select your DE")
    de = c.DE_LIST[select_one(c.DE_LIST)]

    # 1. native package management

    display_title("Native Package Management")

    if distro == "debian":
        BashScript(
            "Backup sources.list?",
            "sudo cp /etc/apt/sources.list /etc/apt/sources.list.old",
        ).ask_and_execute()

        display_question("Select your Debian branch")
        branch_list = ["do nothing", "stable", "testing", "unstable"]
        selected_branch = branch_list[select_one(branch_list)]
        if selected_branch != "do nothing":
            bash(
                f"sudo cp ./assets/debian/{selected_branch}/sources.list /etc/apt/sources.list"
            )

        BashScript(
            "Update the system? (highly recommended)",
            "sudo apt update -y;sudo apt upgrade -y",
        ).ask_and_execute()

        distro_packages["debian"]["install"].register_and_install()

        distro_packages["debian"]["remove"].register_and_remove()

    # 2. flatpak management

    display_title("Flatpak Management")

    if distro == "debian":
        BashScript(
            "Install flatpak?",
            "sudo apt install -y flatpak",
        ).ask_and_execute()

        BashScript(
            "Add flathub repo?",
            "sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
        ).ask_and_execute()

    distro_packages["common"]["install"].register_and_install()

    # 3. desktop enviroment setup

    display_title("Desktop Enviroment Setup")

    if de == "gnome":
        de_packages["gnome"]["install"].register_and_install()

    # 4. system setup

    display_title("System Setup")

    if distro == "debian":
        BashScript(
            "Add 'MOZ_ENABLE_WAYLAND=1' to environment variables to enable Firefox Wayland?",
            """
                mkdir -p ~/.config/environment.d/
                echo "MOZ_ENABLE_WAYLAND=1" > ~/.config/environment.d/firefox_wayland.conf
            """,
        ).ask_and_execute()

    BashScript(
        "Set bundler to install gems to ~/.gem?",
        "bundle config set --local path '~/.gem'",
    ).ask_and_execute()

    BashScript(
        "Add 'up' alias to ~/.bashrc to maintain system?",
        # only use triple quotes
        """
            echo "alias up='sudo apt update -y;sudo apt upgrade -y;sudo apt autoremove -y;flatpak update -y'" >> ~/.bashrc
        """,
    ).ask_and_execute()
    BashScript(
        # [Enable Function Keys On Keychron/Various Mechanical Keyboards Under Linux, with systemd](https://github.com/adam-savard/keyboard-function-keys-linux)
        "Fix keyboard Fn issue? (https://github.com/adam-savard/keyboard-function-keys-linux)",
        """
            sudo cp ./assets/keychron.service /etc/systemd/system/keychron.service
            sudo systemctl enable keychron
            sudo systemctl start keychron
        """,
    ).ask_and_execute()
    BashScript(
        "firmware update with fwupdmgr?",
        # no -y option!! must be confirmed by user
        "sudo fwupdmgr update",
    ).ask_and_execute()
