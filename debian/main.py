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

    # 2. manual package management

    helpers.display_title("Manual Package Management")

    helpers.display_question("Select manual packages to install")
    selected_manual_packages = helpers.select_multiple_strings(
        debian.constants.MANUAL_PACKAGES
    )
    if type(selected_manual_packages) == list:
        for package in selected_manual_packages:
            subprocess.run(package.install, shell=True)

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
        "Setup virt-manager?(add user to libvirt group, start default network)"
    )
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo usermod -a -G libvirt $(whoami)
sudo virsh net-autostart default
sudo virsh net-start default
""",
            shell=True,
        )

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
