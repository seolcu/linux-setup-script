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

    display_title("APT Management")

    display_question("Add contrib and non-free repos?")
    if no_or_yes():
        run(
            "sudo cp ./assets/debian/stable/sources.list /etc/apt/sources.list",
            shell=True,
        )

    display_question("Update the system? (highly recommended)")
    if no_or_yes():
        run("sudo apt update -y; sudo apt upgrade -y", shell=True)

    display_question("Select native packages to install")
    selected_apt_packages = select_multiple_strings(c.APT_PACKAGES)
    if type(selected_apt_packages) == list:
        run(["sudo", "apt", "install", "-y"] + selected_apt_packages)

    display_question("Install virt-manager?")
    if no_or_yes():
        run(
            """
sudo apt install -y virt-manager
sudo usermod -a -G libvirt $(whoami)
sudo virsh net-autostart default
sudo virsh net-start default
""",
            shell=True,
        )
    display_question("Install VSCode?")
    if no_or_yes():
        run(
            """
sudo apt-get install wget gpg -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt install apt-transport-https -y
sudo apt update -y
sudo apt install code -y
""",
            shell=True,
        )

    display_question("Install NeoVIM(AppImage)?")
    if no_or_yes():
        run(
            """
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage
sudo mv nvim.appimage /usr/local/bin/nvim
sudo chmod +x /usr/local/bin/nvim
CUSTOM_NVIM_PATH=/usr/local/bin/nvim
set -u
sudo update-alternatives --install /usr/bin/ex ex "${CUSTOM_NVIM_PATH}" 110
sudo update-alternatives --install /usr/bin/vi vi "${CUSTOM_NVIM_PATH}" 110
sudo update-alternatives --install /usr/bin/view view "${CUSTOM_NVIM_PATH}" 110
sudo update-alternatives --install /usr/bin/vim vim "${CUSTOM_NVIM_PATH}" 110
sudo update-alternatives --install /usr/bin/vimdiff vimdiff "${CUSTOM_NVIM_PATH}" 110
""",
            shell=True,
        )

    display_question("Install ProtonVPN?")
    if no_or_yes():
        run(
            """
wget -P . -O protonvpn.deb https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3-2_all.deb
sudo apt install -f -y ./protonvpn.deb
rm ./protonvpn.deb
sudo apt update -y
sudo apt install -y proton-vpn-gnome-desktop
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

    display_question("Install flatpak?")
    if no_or_yes():
        run("sudo apt install -y flatpak", shell=True)

    display_question("Add flatpak integration to GNOME Software?")
    if no_or_yes():
        run(
            "sudo apt install -y gnome-software-plugin-flatpak",
            shell=True,
        )

    display_question("Add flathub repo?")
    if no_or_yes():
        run(
            "sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
            shell=True,
        )

    display_question("Select flatpak packages to install")
    selected_flatpak_packages = select_multiple_strings(c.FLATPAK_PACKAGES)
    if type(selected_flatpak_packages) == list:
        run(["flatpak", "install", "-y"] + selected_flatpak_packages)

    # 3. misc

    display_title("Misc.")

    display_question(
        "Add 'MOZ_ENABLE_WAYLAND=1' to environment variables to enable Firefox Wayland?"
    )
    if no_or_yes():
        run(
            """
mkdir -p ~/.config/environment.d/
echo "MOZ_ENABLE_WAYLAND=1" > ~/.config/environment.d/firefox_wayland.conf
""",
            shell=True,
        )

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
