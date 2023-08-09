#!./venv/bin/python3

from functions import (
    display_title,
    fix_keyboard,
    switch_to_debian_sid,
    register_all,
    apt_update,
    proceed_all,
)


def main():
    fix_keyboard()
    switch_to_debian_sid()
    register_all()

    display_title("Done! Now wait a moment...")

    apt_update()
    proceed_all()


if __name__ == "__main__":
    main()
