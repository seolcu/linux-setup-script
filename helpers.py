from colorama import Fore, Style
from subprocess import run
from simple_term_menu import TerminalMenu
import constants as c


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
    distro = select_one(c.DISTRO_LIST)
    display_title("Select your DE")
    de = select_one(c.DE_LIST)

    # register install
    c.DISTRO_PACKAGES["common"]["install"].register()
    c.DISTRO_PACKAGES[distro]["install"].register()
    c.DE_PACKAGES[de]["install"].register()

    # register remove
    c.DISTRO_PACKAGES["common"]["remove"].register()
    c.DISTRO_PACKAGES[distro]["remove"].register()
    c.DE_PACKAGES[de]["remove"].register()

    # bash scripts - before process
    c.DISTRO_SCRIPTS["common"]["before"].execute()
    c.DISTRO_SCRIPTS[distro]["before"].execute()

    # installation process
    c.DISTRO_PACKAGES["common"]["install"].install()
    c.DISTRO_PACKAGES[distro]["install"].install()
    c.DE_PACKAGES[de]["install"].install()

    # removal process
    c.DISTRO_PACKAGES["common"]["remove"].remove()
    c.DISTRO_PACKAGES[distro]["remove"].remove()
    c.DE_PACKAGES[de]["remove"].remove()

    # bash scripts - after process
    c.DISTRO_SCRIPTS["common"]["after"].execute()
    c.DISTRO_SCRIPTS[distro]["after"].execute()
