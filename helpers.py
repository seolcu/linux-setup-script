from colorama import Fore, Style
from simple_term_menu import TerminalMenu


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
