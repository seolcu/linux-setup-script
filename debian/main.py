import helpers
import subprocess
import debian.constants


def main():
    # 1. apt management

    helpers.display_title("APT Management")

    helpers.display_question("Add contrib and non-free repos?")
    if helpers.no_or_yes():
        subprocess.run(
            "sudo cp debian/sources.list /etc/apt/sources.list",
            shell=True,
        )

    helpers.display_question("Update the system? (highly recommended)")
    if helpers.no_or_yes():
        subprocess.run("sudo apt update -y; sudo apt upgrade -y", shell=True)

    helpers.display_question("Select native packages to install")
    selected_apt_packages = helpers.select_multiple_strings(
        debian.constants.APT_PACKAGES
    )
    if type(selected_apt_packages) == list:
        subprocess.run(["sudo", "apt", "install", "-y"] + selected_apt_packages)

    helpers.display_question("Select native packages to remove")
    selected_apt_remove_packages = helpers.select_multiple_strings(
        debian.constants.APT_REMOVE_PACKAGES
    )
    if type(selected_apt_remove_packages) == list:
        subprocess.run(
            ["sudo", "apt", "autoremove", "-y"] + selected_apt_remove_packages
        )

    # 2. manual package management

    helpers.display_title("Manual Package Management")

    helpers.display_question("Install VSCode?")
    if helpers.no_or_yes():
        subprocess.run(
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

    helpers.display_question("Install ProtonVPN?")
    if helpers.no_or_yes():
        subprocess.run(
            """
wget -P . -O protonvpn.deb https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3-2_all.deb
sudo apt install -f -y ./protonvpn.deb
rm ./protonvpn.deb
sudo apt update -y
sudo apt install -y proton-vpn-gnome-desktop
""",
            shell=True,
        )

    # 3. flatpak management

    helpers.display_title("Flatpak Management")

    helpers.display_question("Add flathub repo?")
    if helpers.no_or_yes():
        subprocess.run(
            "sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
            shell=True,
        )

    helpers.display_question("Select flatpak packages to install")
    selected_flatpak_packages = helpers.select_multiple_strings(
        debian.constants.FLATPAK_PACKAGES
    )
    if type(selected_flatpak_packages) == list:
        subprocess.run(["flatpak", "install", "-y"] + selected_flatpak_packages)

    # 4. misc

    helpers.display_title("Misc.")

    helpers.display_question(
        "Add 'MOZ_ENABLE_WAYLAND=1' to environment variables to enable Firefox Wayland?"
    )
    if helpers.no_or_yes():
        subprocess.run(
            """
mkdir -p ~/.config/environment.d/
echo "MOZ_ENABLE_WAYLAND=1" > ~/.config/environment.d/firefox_wayland.conf
""",
            shell=True,
        )
