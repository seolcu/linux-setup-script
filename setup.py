#!./venv/bin/python3

from subprocess import run
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
from package_list import (
    manual_install_packages,
    flathub_install_packages,
    apt_install_packages,
    apt_remove_packages,
)


def display_title(title: str):
    print(Fore.GREEN + f"[!] {title}")
    print(Style.RESET_ALL, end="")


def main():
    # [Enable Function Keys On Keychron/Various Mechanical Keyboards Under Linux, with systemd](https://github.com/adam-savard/keyboard-function-keys-linux)
    display_title(
        "Fix keyboard Fn keys issue? (https://github.com/adam-savard/keyboard-function-keys-linux)"
    )
    if TerminalMenu(["No", "Yes"]).show():
        run(
            """
                cp ./keychron.service /etc/systemd/system/keychron.service
                systemctl enable keychron
                systemctl start keychron
            """,
            shell=True,
        )

    display_title("Switch to Debian sid?")
    if TerminalMenu(["No", "Yes"]).show():
        run(
            """
                mv /etc/apt/sources.list /etc/apt/sources.list.old
                cp ./sources.list /etc/apt/sources.list
            """,
            shell=True,
        )

    display_title("Select manual packages to install")
    manual_install_packages.register()

    display_title("Select flathub packages to install")
    flathub_install_packages.register()

    display_title("Select apt packages to install")
    apt_install_packages.register()

    display_title("Select apt packages to remove")
    apt_remove_packages.register()

    display_title("Done! Now wait a moment...")

    display_title("Updating the system")
    run(
        """
            apt update
            apt full-upgrade -y
        """,
        shell=True,
    )

    display_title("Setting up flatpak & flathub")
    run(
        """
            apt install -y flatpak gnome-software-plugin-flatpak
            flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
        """,
        shell=True,
    )

    display_title("Installing packages")
    manual_install_packages.install()
    flathub_install_packages.install()
    apt_install_packages.install()

    display_title("Removing packages")
    apt_remove_packages.remove()
    run("apt autoremove -y", shell=True)


if __name__ == "__main__":
    main()
