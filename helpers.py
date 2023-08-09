from colorama import Fore, Style
from subprocess import run
from simple_term_menu import TerminalMenu
from constants import DISTRO_LIST, DE_LIST, DISTRO_PACKAGES, DE_PACKAGES, DISTRO_SCRIPTS


# Classes


class package:
    name: str
    install_command: str
    remove_command: str

    # is_install: 0 is remove, 1 is install
    def process(self, is_install):
        if is_install:
            run(self.install_command, shell=True)
        else:
            run(self.remove_command, shell=True)

    def install(self):
        self.process(True)

    def remove(self):
        self.process(False)


class manual_package(package):
    def __init__(
        self,
        name: str,
        install_command: str,
        remove_command: str,
    ):
        self.name: str = name
        self.install_command: str = install_command
        self.remove_command: str = remove_command


class flathub_package(package):
    def __init__(self, url: str):
        self.url: str = url
        self.name: str = f"Flathub: {url}"
        self.install_command: str = f"flatpak install flathub {url}"
        self.remove_command: str = f"flatpak remove {url}"


class apt_package(package):
    def __init__(self, apt_name: str):
        self.apt_name: str = apt_name
        self.name: str = f"apt: {apt_name}"
        self.install_command: str = f"sudo apt install {apt_name}"
        self.remove_command: str = f"sudo apt remove {apt_name}"


class dnf_package(package):
    def __init__(self, dnf_name: str):
        self.dnf_name: str = dnf_name
        self.name: str = f"dnf: {dnf_name}"
        self.install_command: str = f"sudo dnf install {dnf_name}"
        self.remove_command: str = f"sudo dnf remove {dnf_name}"


class gnome_extension_package(package):
    def __init__(self, url: str):
        self.url: str = url
        self.name: str = f"GNOME Extension: {url}"
        self.install_command: str = f"gext install {url}"
        self.remove_command: str = f"gext uninstall {url}"


class package_list:
    registered_indexes: int | tuple[int] | None

    # selecting packages for process
    def register(self, is_install: bool = True):
        if is_install:
            display_title("Select packages to install")
        else:
            display_title("Select packages to remove")
        self.registered_indexes = TerminalMenu(
            map(lambda a_package: a_package.name, self.raw_package_list),
            multi_select=True,
            show_multi_select_hint=True,
            multi_select_select_on_accept=False,
            multi_select_empty_ok=True,
        ).show()

    def is_registered(self):
        if type(self.registered_indexes) == None:
            return False
        else:
            return True

    def process(self, is_install):
        if self.is_registered():
            if type(self.registered_indexes) == int:
                index = self.registered_indexes
                self.raw_package_list[index].process(is_install)
            elif type(self.registered_indexes) == tuple[int]:
                for index in self.registered_indexes:
                    self.raw_package_list[index].process(is_install)
        else:
            print("No packages registered")

    def install(self):
        self.process(True)

    def remove(self):
        self.process(False)

    def __init__(self, raw_package_list: list[package]):
        self.raw_package_list: list[package] = raw_package_list


class bash_script:
    def execute(self):
        display_title(self.name)
        if self.ask:
            if no_or_yes():
                run(self.command, shell=True)
        else:
            run(self.command, shell=True)

    def __init__(self, name: str, command: str, ask: bool = False):
        self.name: str = name
        self.command: str = command
        self.ask: bool = ask


class bash_script_list:
    def execute(self):
        for a_script in self.raw_script_list:
            a_script.execute()

    def __init__(self, raw_script_list: list[bash_script]):
        self.raw_script_list: list[bash_script] = raw_script_list


# Functions


def display_title(title: str):
    print(Fore.GREEN + f"[!] {title}", end=f"{Style.RESET_ALL}\n")


def no_or_yes():
    ans: int | tuple[int] | None = TerminalMenu(["No", "Yes"]).show()
    if type(ans) == int:
        return ans
    else:
        return 0


def select_one(options: list[str]):
    index: int | tuple[int] | None = TerminalMenu(options).show()
    if type(index) == int:
        return options[index]
    else:
        return ""


# Main


def main():
    display_title("Select your distro")
    distro = select_one(DISTRO_LIST)
    display_title("Select your DE")
    de = select_one(DE_LIST)

    # register install
    DISTRO_PACKAGES["common"]["install"].register()
    DISTRO_PACKAGES[distro]["install"].register()
    DE_PACKAGES[de]["install"].register()

    # register remove
    DISTRO_PACKAGES["common"]["remove"].register()
    DISTRO_PACKAGES[distro]["remove"].register()
    DE_PACKAGES[de]["remove"].register()

    # bash scripts - before process
    DISTRO_SCRIPTS["common"]["before"].execute()
    DISTRO_SCRIPTS[distro]["before"].execute()

    # installation process
    DISTRO_PACKAGES["common"]["install"].install()
    DISTRO_PACKAGES[distro]["install"].install()
    DE_PACKAGES[de]["install"].install()

    # removal process
    DISTRO_PACKAGES["common"]["remove"].remove()
    DISTRO_PACKAGES[distro]["remove"].remove()
    DE_PACKAGES[de]["remove"].remove()

    # bash scripts - after process
    DISTRO_SCRIPTS["common"]["after"].execute()
    DISTRO_SCRIPTS[distro]["after"].execute()
