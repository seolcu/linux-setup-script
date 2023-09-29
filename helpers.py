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
    def process(self, is_install: bool):
        if is_install:
            bash(self.install_command)
        else:
            bash(self.remove_command)

    def install(self):
        self.process(True)

    def remove(self):
        self.process(False)


class ManualPackage(Package):
    def __init__(
        self,
        name: str,
        install_command: str,
        remove_command: str,
    ):
        self.name: str = f"manaul: {name}"
        self.install_command: str = install_command
        self.remove_command: str = remove_command


class FlatpakPackage(Package):
    def __init__(self, url: str):
        self.url: str = url
        self.name: str = f"flatpak: {url}"
        self.install_command: str = f"flatpak install -y {url}"
        self.remove_command: str = f"flatpak remove -y {url}"


class AptPackage(Package):
    def __init__(self, apt_name: str):
        self.apt_name: str = apt_name
        self.name: str = f"apt: {apt_name}"
        self.install_command: str = f"sudo apt install -y {apt_name}"
        self.remove_command: str = f"sudo apt remove -y {apt_name}"


class DnfPackage(Package):
    def __init__(self, dnf_name: str):
        self.dnf_name: str = dnf_name
        self.name: str = f"dnf: {dnf_name}"
        self.install_command: str = f"sudo dnf install -y {dnf_name}"
        self.remove_command: str = f"sudo dnf remove -y {dnf_name}"


class GnomeExtensionPackage(Package):
    def __init__(self, url: str):
        self.url: str = url
        self.name: str = f"GNOME Extension: {url}"
        self.install_command: str = f"gext install {url}"
        self.remove_command: str = f"gext uninstall {url}"


class PackageList:
    def register(self, is_install: bool = True):
        if len(self.raw_package_list) != 0:
            display_question(
                f"Select packages to {'install' if is_install else 'remove'}"
            )

            self.registered_indexes = TerminalMenu(
                map(lambda a_package: a_package.name, self.raw_package_list),
                multi_select=True,
                show_multi_select_hint=True,
                multi_select_select_on_accept=False,
                multi_select_empty_ok=True,
            ).show()

    def process(self, is_install: bool = True):
        if type(self.registered_indexes) == None:
            display_warning("No packages registered")
        elif type(self.registered_indexes) == int:
            index = self.registered_indexes
            self.raw_package_list[index].process(is_install)
        elif type(self.registered_indexes) == tuple:
            for index in self.registered_indexes:
                self.raw_package_list[index].process(is_install)

    def register_and_process(self, is_install: bool = True):
        self.register(is_install)
        self.process(is_install)

    def register_and_install(self):
        self.register_and_process(is_install=True)

    def register_and_remove(self):
        self.register_and_process(is_install=False)

    def __init__(self, raw_package_list: list[Package]):
        self.raw_package_list: list[Package] = raw_package_list


class BashScript:
    def execute(self):
        display_question(self.question)
        if no_or_yes():
            bash(self.command)

    def __init__(self, question: str, command: str):
        self.question: str = question
        self.command: str = command


# Functions


def display_title(title: str):
    print(Fore.GREEN + f"[!] {title}", end=f"{Style.RESET_ALL}\n")


def display_question(question: str):
    print(Fore.BLUE + question, end=f"{Style.RESET_ALL}\n")


def display_warning(warning: str):
    print(Fore.YELLOW + warning, end=f"{Style.RESET_ALL}\n")


def no_or_yes():
    ans: int | tuple[int, ...] | None = TerminalMenu(["No", "Yes"]).show()
    if type(ans) == int:
        return ans
    else:
        return 0


def select_one(options: list[str]):
    index: int | tuple[int, ...] | None = TerminalMenu(options).show()
    if type(index) == int:
        return options[index]
    else:
        return ""


def bash(command: str):
    run(command, shell=True)


# Instances

distro_packages: dict[str, dict[str, PackageList]] = {
    "common": {
        "install": PackageList(
            [
                FlatpakPackage("com.discordapp.Discord"),
                FlatpakPackage("com.github.tchx84.Flatseal"),
                FlatpakPackage("com.github.unrud.VideoDownloader"),
                FlatpakPackage("com.github.ztefn.haguichi"),
                FlatpakPackage("com.microsoft.Edge"),
                FlatpakPackage("com.mojang.Minecraft"),
                FlatpakPackage("com.obsproject.Studio"),
                FlatpakPackage("com.protonvpn.www"),
                FlatpakPackage("com.rafaelmardojai.Blanket"),
                FlatpakPackage("com.spotify.Client"),
                FlatpakPackage("com.usebottles.bottles"),
                FlatpakPackage("com.valvesoftware.Steam"),
                FlatpakPackage("de.haeckerfelix.Fragments"),
                FlatpakPackage("in.srev.guiscrcpy"),
                FlatpakPackage("io.mrarm.mcpelauncher"),
                FlatpakPackage("md.obsidian.Obsidian"),
                FlatpakPackage("org.gabmus.whatip"),
                FlatpakPackage("org.gimp.GIMP"),
                FlatpakPackage("org.gnome.NetworkDisplays"),
                FlatpakPackage("org.kde.kdenlive"),
                FlatpakPackage("org.onlyoffice.desktopeditors"),
                FlatpakPackage("org.raspberrypi.rpi-imager"),
                FlatpakPackage("org.remmina.Remmina"),
                FlatpakPackage("org.videolan.VLC"),
                FlatpakPackage("us.zoom.Zoom"),
            ]
        ),
    },
    "debian": {
        "install": PackageList(
            [
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
                AptPackage("gnome-software-plugin-flatpak"),
                AptPackage("gcc"),
                AptPackage("g++"),
                AptPackage("default-jdk"),
                AptPackage("python3-pip"),
                AptPackage("python3-venv"),
                AptPackage("python3-ipykernel"),
                AptPackage("black"),
                ManualPackage(
                    "nvm",
                    """
                        sudo apt install -y curl
                        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
                    """,
                    "",
                ),
                AptPackage("curl"),
                AptPackage("wget"),
                AptPackage("gpg"),
                AptPackage("htop"),
                AptPackage("neofetch"),
                AptPackage("gh"),
                AptPackage("solaar"),
                AptPackage("python3-nautilus"),
                AptPackage("distrobox"),
                AptPackage("timeshift"),
            ]
        ),
        "remove": PackageList(
            [
                AptPackage("gnome-games"),
                AptPackage("rhythmbox"),
                AptPackage("evolution"),
                AptPackage("zutty"),
                AptPackage("shotwell"),
            ]
        ),
    },
    "fedora": {
        "install": PackageList(
            [
                DnfPackage("naver-nanum-gothic-fonts"),
                ManualPackage(
                    "vscode",
                    """
                        sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
                        sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
                        dnf check-update
                        sudo dnf install -y code
                    """,
                    "sudo dnf remove -y code",
                ),
                DnfPackage("gcc"),
                DnfPackage("g++"),
                DnfPackage("java-latest-openjdk"),
                ManualPackage(
                    "manual: nvm",
                    """
                        sudo dnf install -y curl
                        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
                    """,
                    "",
                ),
                DnfPackage("curl"),
                DnfPackage("wget"),
                DnfPackage("gpg"),
                DnfPackage("htop"),
                DnfPackage("neofetch"),
                DnfPackage("gh"),
                DnfPackage("solaar"),
                DnfPackage("nautilus-python"),
                DnfPackage("nautilus-extensions"),
                DnfPackage("evolution-data-server"),
                DnfPackage("distrobox"),
                DnfPackage("libva-utils"),
                FlatpakPackage("org.gnome.Music"),
            ]
        ),
        "remove": PackageList([DnfPackage("rhythmbox")]),
    },
}


de_packages: dict[str, dict[str, PackageList]] = {
    "gnome": {
        "install": PackageList(
            [
                GnomeExtensionPackage("appindicatorsupport@rgcjonas.gmail.com"),
                GnomeExtensionPackage("caffeine@patapon.info"),
                GnomeExtensionPackage("gsconnect@andyholmes.github.io"),
                GnomeExtensionPackage("gestureImprovements@gestures"),
                GnomeExtensionPackage("Vitals@CoreCoding.com"),
                GnomeExtensionPackage("clipboard-indicator@tudmotu.com"),
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
    distro = select_one(c.DISTRO_LIST)
    display_question("Select your DE")
    de = select_one(c.DE_LIST)

    # 1. native package management

    display_title("Native Package Management")

    if distro == "debian":
        BashScript(
            "Backup sources.list?",
            "sudo cp /etc/apt/sources.list /etc/apt/sources.list.old",
        ).execute()

        display_question("Select your Debian branch")
        branch = select_one(["do nothing", "stable", "testing", "unstable"])
        if branch != "do nothing":
            bash(f"sudo cp ./assets/debian/{branch}/sources.list /etc/apt/sources.list")

        BashScript(
            "Update the system? (highly recommended)",
            "sudo apt update -y;sudo apt upgrade -y",
        ).execute()

        distro_packages["debian"]["install"].register_and_install()

        distro_packages["debian"]["remove"].register_and_remove()

        BashScript(
            "Autoremove?",
            "sudo apt autoremove -y",
        ).execute()

    elif distro == "fedora":
        BashScript(
            "Backup dnf.conf?", "sudo cp /etc/dnf/dnf.conf /etc/dnf/dnf.conf.old"
        ).execute()

        BashScript(
            "Edit dnf.conf to make it faster?",
            "sudo cp ./assets/fedora/dnf.conf /etc/dnf/dnf.conf",
        ).execute()

        BashScript(
            "Enable RPM Fusion?",
            """
                sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
                sudo dnf groupupdate -y core
            """,
        ).execute()

        BashScript(
            "Update the system? (highly recommended)", "sudo dnf update -y"
        ).execute()

        BashScript(
            "Switch to full ffmpeg?",
            "sudo dnf swap -y ffmpeg-free ffmpeg --allowerasing",
        ).execute()

        BashScript(
            "Install codecs? (No VAAPI codecs included))",
            """
                sudo dnf groupupdate -y multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
                sudo dnf groupupdate -y sound-and-video
            """,
        ).execute()

        BashScript(
            "Install VAAPI codecs for Intel(recent)?",
            "sudo dnf install -y intel-media-driver",
        ).execute()

        BashScript(
            "Install VAAPI codecs for Intel(older)?",
            "sudo dnf install -y libva-intel-driver",
        ).execute()

        BashScript(
            "Install VAAPI codecs for AMD(mesa)?",
            """
                sudo dnf swap -y mesa-va-drivers mesa-va-drivers-freeworld
                sudo dnf swap -y mesa-vdpau-drivers mesa-vdpau-drivers-freeworld
                
            """,
        ).execute()

        BashScript(
            "Install VAAPI codecs for AMD(mesa) - i686?",
            """
                sudo dnf swap -y mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686
                sudo dnf swap -y mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686
            """,
        ).execute()

        BashScript(
            "Install VAAPI codecs for NVIDIA?",
            "sudo dnf install -y nvidia-vaapi-driver",
        ).execute()

        distro_packages["fedora"]["install"].register_and_install()
        distro_packages["fedora"]["remove"].register_and_remove()

    # 2. flatpak management

    display_title("Flatpak Management")

    if distro == "debian":
        BashScript(
            "Install flatpak?",
            "sudo apt install -y flatpak",
        ).execute()

        BashScript(
            "Add flathub repo?",
            "sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
        ).execute()

    distro_packages["common"]["install"].register_and_install()

    # 3. desktop enviroment setup

    display_title("Desktop Enviroment Setup")

    if de == "gnome":
        de_packages["gnome"]["install"].register_and_install()

    # 4. system setup

    display_title("System Setup")

    if distro == "fedora":
        BashScript(
            "Change the hostname?",
            """
                echo "type new hostname"
                read input
                sudo hostnamectl set-hostname $input
            """,
        ).execute()

    if distro == "debian":
        BashScript(
            "Add 'MOZ_ENABLE_WAYLAND=1' to environment variables to enable Firefox Wayland?",
            """
                mkdir -p ~/.config/environment.d/
                echo "MOZ_ENABLE_WAYLAND=1" > ~/.config/environment.d/firefox_wayland.conf
            """,
        ).execute()

    BashScript(
        "Add 'up' alias to ~/.bashrc to maintain system?",
        # only use triple quotes
        """
            echo "alias up='sudo apt update -y;sudo apt upgrade -y;sudo apt autoremove -y;flatpak update -y'" >> ~/.bashrc
        """,
    ).execute()
    BashScript(
        # [Enable Function Keys On Keychron/Various Mechanical Keyboards Under Linux, with systemd](https://github.com/adam-savard/keyboard-function-keys-linux)
        "Fix keyboard Fn issue? (https://github.com/adam-savard/keyboard-function-keys-linux)",
        """
            sudo cp ./assets/keychron.service /etc/systemd/system/keychron.service
            sudo systemctl enable keychron
            sudo systemctl start keychron
        """,
    ).execute()
    BashScript(
        "firmware update with fwupdmgr?",
        # no -y option!! must be confirmed by user
        "sudo fwupdmgr update",
    ).execute()
