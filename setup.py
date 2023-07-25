#!./venv/bin/python3

from subprocess import run
from colorama import Fore, Style

step = 0


def display_title(title):
    global step
    step += 1
    print(Fore.GREEN + "========== (%d) %s ==========" % (step, title))
    print(Style.RESET_ALL, end="")


class package:
    def __init__(self, name, desc, default):
        self.name = name
        self.desc = desc
        self.default = default


class native_package(package):
    def __init__(self, name, desc, default, apt_name):
        super().__init__(name, desc, default)
        self.apt_name = apt_name


class flatpak_package(package):
    def __init__(self, name, desc, default, url):
        super().__init__(name, desc, default)
        self.url = url


display_title("Switching to Debian sid")
ans = input("Switch to Debian sid? [y/N]: ")
if ans == "y" or ans == "Y":
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
    native_package(
        "essentials",
        "git, gcc, g++, curl, wget, gpg",
        True,
        "git gcc g++ curl wget gpg",
    ),
    native_package("htop", "cli system monitor", True, "htop"),
    native_package("neofetch", "fetch script", True, "neofetch"),
    native_package(
        "solaar",
        "manages Logitech receivers, keyboards, mice, and tablets",
        False,
        "solaar",
    ),
    native_package("python3-nautilus", "for GSConnect", False, "python3-nautilus"),
    native_package("steam-devices", "steam controller support", False, "steam-devices"),
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
    native_package("gnome games", "gnome default games", True, "gnome-games"),
    native_package("rhythmbox", "music player", True, "rhythmbox"),
    native_package("evolution", "mail client", True, "evolution"),
    native_package("zutty", "terminal", True, "zutty"),
    native_package("shotwell", "image manager", True, "shotwell"),
    native_package("transmission", "torrent client", True, "transmission-common"),
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
    flatpak_package("Spotify", "music streaming service", False, "com.spotify.Client"),
    flatpak_package("VLC", "video player", True, "org.videolan.VLC"),
    flatpak_package("MS Edge", "web browser", False, "com.microsoft.Edge"),
    flatpak_package(
        "Flatseal", "flatpak permission manager", False, "com.github.tchx84.Flatseal"
    ),
    flatpak_package(
        "Gnome Extension Manager",
        "manage gnome extension easily",
        True,
        "com.mattjakeman.ExtensionManager",
    ),
    flatpak_package("Bottles", "wine env manager", True, "com.usebottles.bottles"),
    flatpak_package("Zoom", "video conferencing", False, "us.zoom.Zoom"),
    flatpak_package(
        "Video Downloader",
        "download YT video easily",
        False,
        "com.github.unrud.VideoDownloader",
    ),
    flatpak_package("Proton VPN", "privacy respecting vpn", False, "com.protonvpn.www"),
    flatpak_package(
        "Obsidian", "markdown knowledge base", False, "md.obsidian.Obsidian"
    ),
    flatpak_package(
        "Gnome Boxes", "easy KVM virtual machine manager", True, "org.gnome.Boxes"
    ),
    flatpak_package("Remmina", "VNC/RDP client", True, "org.remmina.Remmina"),
    flatpak_package(
        "Gnome Network Display", "miracast support", True, "org.gnome.NetworkDisplays"
    ),
    flatpak_package(
        "Blanket", "white noise player", True, "com.rafaelmardojai.Blanket"
    ),
    flatpak_package("guiscrcpy", "easy gui scrcpy", False, "in.srev.guiscrcpy"),
    flatpak_package("What IP", "ip checker", True, "org.gabmus.whatip"),
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
