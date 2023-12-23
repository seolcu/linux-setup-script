import helpers
import subprocess
import arch.constants


def main():
    # 1. pacman management

    helpers.display_title("pacman Management")

    helpers.display_question("Add multilib repo?")
    if helpers.no_or_yes():
        subprocess.run(
            "sudo cp arch/pacman.conf /etc/pacman.conf",
            shell=True,
        )

    helpers.display_question("Update the system? (highly recommended)")
    if helpers.no_or_yes():
        subprocess.run("sudo pacman -Syu", shell=True)

    helpers.display_question("Select pacman packages to install")
    selected_pacman_packages = helpers.select_multiple_strings(
        arch.constants.PACMAN_PACKAGES
    )
    if type(selected_pacman_packages) == list:
        subprocess.run(["sudo", "pacman", "-S"] + selected_pacman_packages)

    # 2. AUR package management

    helpers.display_title("AUR Package Management")

    helpers.display_question("Install paru(AUR helper)?")
    if helpers.no_or_yes():
        subprocess.run(
            "mkdir ~/문서/AUR; cd ~/문서/AUR; git clone https://aur.archlinux.org/paru-bin.git; cd paru-bin; makepkg -si",
            shell=True,
        )

    helpers.display_question("Select AUR packages to install")
    selected_aur_packages = helpers.select_multiple_strings(arch.constants.AUR_PACKAGES)
    if type(selected_aur_packages) == list:
        subprocess.run(["paru", "-S"] + selected_aur_packages)

    # 3. flatpak management

    helpers.display_title("Flatpak Management")

    helpers.display_question("Select flatpak packages to install")
    selected_flatpak_packages = helpers.select_multiple_strings(
        arch.constants.FLATPAK_PACKAGES
    )
    if type(selected_flatpak_packages) == list:
        subprocess.run(["flatpak", "install", "-y"] + selected_flatpak_packages)
