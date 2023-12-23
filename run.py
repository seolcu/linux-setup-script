#!/usr/bin/env python3


if __name__ == "__main__":
    import setup

    setup.setup()

    import helpers

    helpers.display_title("Welcome to the package manager")
    helpers.display_title("Setting up the environment")
    helpers.display_question("What distro are you using?")
    distro = helpers.select_one_string("arch", "debian")
    if distro == "arch":
        import arch

        arch.main.main()
    elif distro == "debian":
        import debian.main

        debian.main.main()
    else:
        helpers.display_error("Unknown distro")
        exit(1)
