#!venv/bin/python3

import helpers
import setup

if __name__ == "__main__":
    helpers.display_title("Welcome to the package manager")
    helpers.display_title("Setting up the environment")
    setup.setup()
    helpers.display_question("What distro are you using?")
    distro = helpers.select_one_string("arch", "debian")
    if distro == "arch":
        import arch

        arch.main()
    elif distro == "debian":
        import debian.main as main

        main.main()
    else:
        helpers.display_error("Unknown distro")
        exit(1)
