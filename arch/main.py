def main():
    helpers.display_title("Installing packages")
    helpers.display_question("What packages do you want to install?")
    packages = helpers.select_multiple_strings("firefox", "chromium", "git", "vim", "emacs", "python3", "python3-pip", "python3-venv", "python3-dev", "python3-setuptools", "python3-wheel", "python3-pytest", "python3-pytest-cov", "python3-pytest-xdist", "python3-pytest-mock", "python3-pyte