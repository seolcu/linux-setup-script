import helpers
import subprocess
import fedora.constants


def main():
    # 1. dnf management

    helpers.display_title("DNF Management")

    helpers.display_question("Update the system? (highly recommended)")
    if helpers.no_or_yes():
        subprocess.run("sudo dnf update -y", shell=True)

    helpers.display_question("Select native packages to install")
    selected_dnf_packages = helpers.select_multiple_strings(
        fedora.constants.DNF_PACKAGES
    )
    if type(selected_dnf_packages) == list:
        subprocess.run(["sudo", "dnf", "install", "-y"] + selected_dnf_packages)

    helpers.display_question("Select native packages to remove")
    selected_dnf_remove_packages = helpers.select_multiple_strings(
        fedora.constants.DNF_REMOVE_PACKAGES
    )
    if type(selected_dnf_remove_packages) == list:
        subprocess.run(["sudo", "dnf", "remove", "-y"] + selected_dnf_remove_packages)

    # 2. RPM Fusion

    helpers.display_title("RPM Fusion")

    helpers.display_question("Enable RPM Fusion?")
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager --enable fedora-cisco-openh264
sudo dnf groupupdate core -y
""",
            shell=True,
        )

    helpers.display_question(
        "Install additional packages for multimedia from RPM Fusion? (No VAAPI)"
    )
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo dnf swap ffmpeg-free ffmpeg --allowerasing -y
sudo dnf groupupdate multimedia --setopt="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin -y
sudo dnf groupupdate sound-and-video -y
sudo dnf install rpmfusion-free-release-tainted -y
sudo dnf install libdvdcss -y
sudo dnf install rpmfusion-nonfree-release-tainted -y
sudo dnf --repo=rpmfusion-nonfree-tainted install "*-firmware" -y
""",
            shell=True,
        )

    helpers.display_question("Install VAAPI for Intel(recent)?")
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo dnf install intel-media-driver -y
""",
            shell=True,
        )

    helpers.display_question("Install VAAPI for Intel(older)?")
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo dnf install libva-intel-driver -y
""",
            shell=True,
        )

    helpers.display_question("Install VAAPI for AMD?")
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo dnf swap mesa-va-drivers mesa-va-drivers-freeworld -y
sudo dnf swap mesa-vdpau-drivers mesa-vdpau-drivers-freeworld -y
sudo dnf swap mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686 -y
sudo dnf swap mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686 -y
""",
            shell=True,
        )

    helpers.display_question("Install codecs for NVIDIA? (No VAAPI")
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo dnf install nvidia-vaapi-driver
""",
            shell=True,
        )

    # 3. manual package management

    helpers.display_title("Manual Package Management")

    helpers.display_question("Install VSCode?")
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
dnf check-update -y
sudo dnf install code -y
""",
            shell=True,
        )

    helpers.display_question("Install ProtonVPN?")
    if helpers.no_or_yes():
        subprocess.run(
            """
wget https://repo.protonvpn.com/fedora-39-stable/protonvpn-stable-release/protonvpn-stable-release-1.0.1-2.noarch.rpm
sudo dnf install ./protonvpn-stable-release-1.0.1-2.noarch.rpm -y
rm ./protonvpn-stable-release-1.0.1-2.noarch.rpm
sudo dnf install --refresh proton-vpn-gnome-desktop -y
""",
            shell=True,
        )

    helpers.display_question("Install NVM?")
    if helpers.no_or_yes():
        subprocess.run(
            """
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
""",
            shell=True,
        )

    helpers.display_question("Install Hugo(extended, v0.122.0)?")
    if helpers.no_or_yes():
        subprocess.run(
            """
mkdir tmp
cd tmp
wget https://github.com/gohugoio/hugo/releases/download/v0.122.0/hugo_extended_0.122.0_linux-amd64.tar.gz
tar -xzf hugo_extended_0.122.0_linux-amd64.tar.gz
sudo mv hugo /usr/local/bin
cd ..
rm -rf tmp
""",
            shell=True,
        )

    helpers.display_question("Install virt-manager?")
    if helpers.no_or_yes():
        subprocess.run(
            """
sudo dnf install virt-manager -y
sudo systemctl enable --now libvirtd
sudo usermod -a -G libvirt $(whoami)
sudo virsh net-autostart default
""",
            shell=True,
        )

    # 4. flatpak management

    helpers.display_title("Flatpak Management")

    helpers.display_question("Select flatpak packages to install")
    selected_flatpak_packages = helpers.select_multiple_strings(
        fedora.constants.FLATPAK_PACKAGES
    )
    if type(selected_flatpak_packages) == list:
        subprocess.run(["flatpak", "install", "-y"] + selected_flatpak_packages)

    # 5. additional tweaks

    helpers.display_title("Additional Tweaks")

    helpers.display_question("Apply git configuration?")
    if helpers.no_or_yes():
        subprocess.run(
            """
git config --global init.defaultBranch main
git config --global push.autoSetupRemote true
""",
            shell=True,
        )
