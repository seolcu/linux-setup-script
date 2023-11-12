from colorama import Fore, Style
from subprocess import run
from simple_term_menu import TerminalMenu
import constants as c


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


def select_one_string(options: list[str]) -> str:
    index: int | tuple[int, ...] | None = TerminalMenu(options).show()
    if type(index) == int:
        return options[index]
    else:
        display_warning("No option selected")
        return select_one_string(options)


def select_multiple_strings(options: list[str]) -> None | list[str]:
    indexes: int | tuple[int, ...] | None = TerminalMenu(
        options,
        multi_select=True,
        show_multi_select_hint=True,
        multi_select_select_on_accept=False,
        multi_select_empty_ok=True,
    ).show()
    if indexes == None:
        display_warning("No packages registered")
        return None
    elif type(indexes) == int:
        return [options[indexes]]
    elif type(indexes) == tuple:
        selected_options_list = []
        for index in indexes:
            selected_options_list.append(options[index])
        return selected_options_list
    else:
        display_warning("Unexpected input")
        return select_multiple_strings(options)


# Main


def main():
    # 0. prepare

    display_title("Welcome to the Linux Setup Script")

    # 1. apt management

    display_title("DNF Management")

    display_question("Update the system? (highly recommended)")
    if no_or_yes():
        run("sudo dnf update -y", shell=True)

    display_question("Add RPMFusion repos?")
    if no_or_yes():
        run(
            "sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm; sudo dnf groupupdate -y core",
            shell=True,
        )

    display_question("Install multimedia packages from RPMFusion?")
    if no_or_yes():
        gpu_type: str = select_one_string(["Intel", "AMD", "NVIDIA", "None"])

        # Common
        run(
            """
sudo dnf swap ffmpeg-free ffmpeg --allowerasing -y
sudo dnf groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin -y
sudo dnf groupupdate sound-and-video -y
sudo dnf install rpmfusion-free-release-tainted -y
sudo dnf install libdvdcss -y
sudo dnf install rpmfusion-nonfree-release-tainted -y
sudo dnf --repo=rpmfusion-nonfree-tainted install "*-firmware" -y
""",
            shell=True,
        )

        match gpu_type:
            case "Intel":
                run("sudo dnf install intel-media-driver -y", shell=True)
            case "AMD":
                run(
                    """
sudo dnf swap mesa-va-drivers mesa-va-drivers-freeworld -y
sudo dnf swap mesa-vdpau-drivers mesa-vdpau-drivers-freeworld -y
sudo dnf swap mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686 -y
sudo dnf swap mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686 -y
""",
                    shell=True,
                )
            case "NVIDIA":
                run("sudo dnf install nvidia-vaapi-driver -y", shell=True)
            case "None":
                display_warning("Not installing any VAAPI drivers")

    display_question("Select native packages to install")
    selected_dnf_packages = select_multiple_strings(c.DNF_PACKAGES)
    if type(selected_dnf_packages) == list:
        run(["sudo", "dnf", "install", "-y"] + selected_dnf_packages)

    display_question("Install VSCode?")
    if no_or_yes():
        run(
            """
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
dnf check-update
sudo dnf install code -y
""",
            shell=True,
        )

    display_question("Install ProtonVPN?")
    if no_or_yes():
        run(
            """
wget https://repo.protonvpn.com/fedora-39-stable/protonvpn-stable-release/protonvpn-stable-release-1.0.1-2.noarch.rpm
sudo dnf install ./protonvpn-stable-release-1.0.1-2.noarch.rpm -y
sudo dnf check-update
sudo dnf upgrade -y
sudo dnf install --refresh proton-vpn-gnome-desktop -y
""",
            shell=True,
        )

    display_question("Install NVM?")
    if no_or_yes():
        run(
            """
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
""",
            shell=True,
        )

    # 2. flatpak management

    display_title("Flatpak Management")

    display_question("Select flatpak packages to install")
    selected_flatpak_packages = select_multiple_strings(c.FLATPAK_PACKAGES)
    if type(selected_flatpak_packages) == list:
        run(["flatpak", "install", "-y"] + selected_flatpak_packages)

    # 3. misc

    display_title("Misc.")

    display_question(
        "Fix keyboard Fn issue? (https://github.com/adam-savard/keyboard-function-keys-linux)"
    )
    if no_or_yes():
        run(
            """
sudo cp ./assets/keychron.service /etc/systemd/system/keychron.service
sudo systemctl enable keychron
sudo systemctl start keychron
""",
            shell=True,
        )

    display_question("firmware update with fwupdmgr?")
    if no_or_yes():
        run("sudo fwupdmgr update", shell=True)
