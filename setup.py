#!./venv/bin/python3

from subprocess import run
from colorama import Fore, Style
from simple_term_menu import TerminalMenu


class package:
    def install(self):
        run(self.install_command, shell=True)

    def remove(self):
        run(self.remove_command, shell=True)

    def __init__(
        self,
        name: str,
        desc: str,
        default: bool,
        install_command: str,
        remove_command: str,
    ):
        self.name = name
        self.desc = desc
        self.default = default
        self.install_command = install_command
        self.remove_command = remove_command


class apt_package(package):
    def __init__(self, name: str, desc: str, default: bool, apt_name: str):
        install_command = f"apt install -y {apt_name}"
        remove_command = f"apt remove -y {apt_name}"
        super().__init__(name, desc, default, install_command, remove_command)


class flatpak_package(package):
    def __init__(self, name: str, desc: str, default: bool, repo: str, url: str):
        install_command = f"flatpak install -y {repo} {url}"
        remove_command = f"flatpak remove -y {url}"
        super().__init__(name, desc, default, install_command, remove_command)


class package_list:
    def install(self):
        for a_package in self.raw_package_list:
            a_package.install()

    def remove(self):
        for a_package in self.raw_package_list:
            a_package.remove()

    def __init__(self, raw_package_list: list[package]):
        self.raw_package_list = raw_package_list


def display_title(title: str):
    global step
    step += 1
    print(Fore.GREEN + f"========== ({step}) {title} ==========")
    print(Style.RESET_ALL, end="")


# input & output: 0(False) or 1(True)
def binary_menu(default_answer: bool):
    global preset_index
    if preset_index == 0:
        return default_answer
    elif preset_index == 1:
        return bool(
            TerminalMenu(["No", "Yes"], cursor_index=int(default_answer)).show()
        )
    elif preset_index == 2:
        return True


def main():
    global step
    step: int = 0

    display_title("Selecting process preset")
    global preset, preset_index, preset_options
    preset_options: list[str] = ["default", "custom", "all yes"]
    preset_index: int = TerminalMenu(preset_options).show()
    preset: str = preset_options[preset_index]

    display_title("Switching to Debian sid")
    print("Switch to Debian sid?")
    if binary_menu(default_answer=False) == True:
        run(
            """
                mv /etc/apt/sources.list /etc/apt/sources.list.old
                cp ./sources.list /etc/apt/sources.list
            """,
            shell=True,
        )

    display_title("Updating the system")
    run(
        """
            apt update
            apt full-upgrade -y
        """,
        shell=True,
    )

    display_title("Installing native packages")
    debian_install_packages = [
        apt_package(
            "essentials",
            "git, gcc, g++, curl, wget, gpg",
            True,
            "git gcc g++ curl wget gpg",
        ),
        apt_package("htop", "cli system monitor", True, "htop"),
        apt_package("neofetch", "fetch script", True, "neofetch"),
        apt_package(
            "solaar",
            "manages Logitech receivers, keyboards, mice, and tablets",
            False,
            "solaar",
        ),
        apt_package("python3-nautilus", "for GSConnect", False, "python3-nautilus"),
        apt_package(
            "steam-devices", "steam controller support", False, "steam-devices"
        ),
    ]

    debian_install_string = "apt install -y "
    for pkg in debian_install_packages:
        print("install %s(%s)?" % (pkg.name, pkg.desc), end=" ")
        if pkg.default == True:
            ans = input("[Y/n]: ")
            if ans != "n" and ans != "N":
                debian_install_string += pkg.apt_name + " "
        elif pkg.default == False:
            ans = input("[y/N]: ")
            if ans == "y" or ans == "Y":
                debian_install_string += pkg.apt_name + " "
    run(debian_install_string, shell=True)

    # manually install VSCode
    ans = input("install Visual Studio Code(code editor)?[Y/n]: ")
    if ans != "n" and ans != "N":
        run(
            """
                apt install -y wget gpg
                wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
                install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
                sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
                rm -f packages.microsoft.gpg
                apt install -y apt-transport-https
                apt update
                apt install -y code
            """,
            shell=True,
        )

    display_title("Remove useless packages")
    debian_remove_packages = [
        apt_package("gnome games", "gnome default games", True, "gnome-games"),
        apt_package("rhythmbox", "music player", True, "rhythmbox"),
        apt_package("evolution", "mail client", True, "evolution"),
        apt_package("zutty", "terminal", True, "zutty"),
        apt_package("shotwell", "image manager", True, "shotwell"),
    ]

    debian_remove_string = "apt remove -y "
    for pkg in debian_remove_packages:
        print("remove %s(%s)?" % (pkg.name, pkg.desc), end=" ")
        if pkg.default == True:
            ans = input("[Y/n]: ")
            if ans != "n" and ans != "N":
                debian_remove_string += pkg.apt_name + " "
        elif pkg.default == False:
            ans = input("[y/N]: ")
            if ans == "y" or ans == "Y":
                debian_remove_string += pkg.apt_name + " "
    run(debian_remove_string, shell=True)
    run("apt autoremove -y", shell=True)

    display_title("Setting up flatpak & flathub")
    run(
        """
            apt install -y flatpak gnome-software-plugin-flatpak
            flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
        """,
        shell=True,
    )

    display_title("Installing flatpak packages")
    flatpak_install_packages = [
        flatpak_package(
            "Spotify", "music streaming service", False, "flathub", "com.spotify.Client"
        ),
        flatpak_package("VLC", "video player", True, "flathub", "org.videolan.VLC"),
        flatpak_package(
            "MS Edge", "web browser", False, "flathub", "com.microsoft.Edge"
        ),
        flatpak_package(
            "Flatseal",
            "flatpak permission manager",
            False,
            "flathub",
            "com.github.tchx84.Flatseal",
        ),
        flatpak_package(
            "Gnome Extension Manager",
            "manage gnome extension easily",
            True,
            "flathub",
            "com.mattjakeman.ExtensionManager",
        ),
        flatpak_package(
            "Bottles", "wine env manager", True, "flathub", "com.usebottles.bottles"
        ),
        flatpak_package("Zoom", "video conferencing", False, "flathub", "us.zoom.Zoom"),
        flatpak_package(
            "Video Downloader",
            "download YT video easily",
            False,
            "flathub",
            "com.github.unrud.VideoDownloader",
        ),
        flatpak_package(
            "Proton VPN",
            "privacy respecting vpn",
            False,
            "flathub",
            "com.protonvpn.www",
        ),
        flatpak_package(
            "Obsidian",
            "markdown knowledge base",
            False,
            "flathub",
            "md.obsidian.Obsidian",
        ),
        flatpak_package(
            "Gnome Boxes",
            "easy KVM virtual machine manager",
            True,
            "flathub",
            "org.gnome.Boxes",
        ),
        flatpak_package(
            "Remmina", "remote desktop client", True, "flathub", "org.remmina.Remmina"
        ),
        flatpak_package(
            "Gnome Network Display",
            "miracast support",
            True,
            "flathub",
            "org.gnome.NetworkDisplays",
        ),
        flatpak_package(
            "Blanket",
            "white noise player",
            True,
            "flathub",
            "com.rafaelmardojai.Blanket",
        ),
        flatpak_package(
            "guiscrcpy", "easy gui scrcpy", False, "flathub", "in.srev.guiscrcpy"
        ),
        flatpak_package("What IP", "ip checker", True, "flathub", "org.gabmus.whatip"),
    ]

    flatpak_install_string = "flatpak install flathub -y "
    for pkg in flatpak_install_packages:
        print("install %s(%s)?" % (pkg.name, pkg.desc), end=" ")
        if pkg.default == True:
            ans = input("[Y/n]: ")
            if ans != "n" and ans != "N":
                flatpak_install_string += pkg.url + " "
        elif pkg.default == False:
            ans = input("[y/N]: ")
            if ans == "y" or ans == "Y":
                flatpak_install_string += pkg.url + " "
    run(flatpak_install_string, shell=True)

    # [Enable Function Keys On Keychron/Various Mechanical Keyboards Under Linux, with systemd](https://github.com/adam-savard/keyboard-function-keys-linux)
    display_title(
        "Function key error fix for some users(https://github.com/adam-savard/keyboard-function-keys-linux)"
    )
    ans = input("Fix keyboard?[y/N]: ")
    if ans == "y" or ans == "Y":
        run(
            """
                cp ./keychron.service /etc/systemd/system/keychron.service
                systemctl enable keychron
                systemctl start keychron
            """,
            shell=True,
        )


if __name__ == "__main__":
    main()
