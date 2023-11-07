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
    if type(indexes) == None:
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

    display_question("Backup sources.list?")
    if no_or_yes():
        run("sudo cp /etc/apt/sources.list /etc/apt/sources.list.old", shell=True)

    display_question("Select your Debian branch")
    selected_branch = select_one_string(["do nothing", "stable", "testing", "unstable"])
    if selected_branch != "do nothing":
        run(
            f"sudo cp ./assets/debian/{selected_branch}/sources.list /etc/apt/sources.list",
            shell=True,
        )

    display_question("Update the system? (highly recommended)")
    if no_or_yes():
        run("sudo apt update -y;sudo apt upgrade -y", shell=True)

    display_question("Select native packages to install")
    selected_apt_packages = select_multiple_strings(c.APT_PACKAGES)
    if type(selected_apt_packages) == list:
        run(["sudo", "apt", "install", "-y"] + selected_apt_packages)

    display_question("Install VSCode?")
    if no_or_yes():
        run(
            """
sudo apt-get install -y wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt install -y apt-transport-https
sudo apt update
sudo apt install -y code
""",
            shell=True,
        )

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

    display_question("Install ProtonVPN?")
    if no_or_yes():
        run(
            """
wget -P . -O protonvpn.deb https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3-2_all.deb
sudo apt install -f -y ./protonvpn.deb
rm ./protonvpn.deb
sudo apt update -y
sudo apt install -y protonvpn
""",
            shell=True,
        )

    display_question("Install NVM?")
    if no_or_yes():
        run(
            """
sudo apt install -y curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
""",
            shell=True,
        )

    # 2. flatpak management

    display_title("Flatpak Management")

    display_question("Install flatpak?")
    if no_or_yes():
        run("sudo apt install -y flatpak", shell=True)

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

    display_question("Set bundler to install gems to ~/.gem?")
    if no_or_yes():
        run("bundle config set --local path '~/.gem'", shell=True)

    display_question("Add 'up' alias to ~/.bashrc to maintain system?")
    if no_or_yes():
        run(
            """
echo "alias up='sudo apt update -y;sudo apt upgrade -y;sudo apt autoremove -y;flatpak update -y'" >> ~/.bashrc
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
