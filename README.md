# linux-setup-script

initial setup script for some distros.
currently support Debian/Fedora, GNOME.

## setup

### 0. requirements

- python3
- python3-venv
- git

### 1. clone this repo

```bash
git clone https://github.com/seolcu/linux-setup-script
cd linux-setup-script
```

### 2. setup python venv

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirement.txt
```

### 3. execute the script

```bash
./run.py
```

### 4. cleanup

```bash
deactivate
cd ..
rm -rf linux-setup-script
```

## documentation: developer manual

### 0. mission

what this script do:

    1. install native packages
    2. setup flatpak
    3. tweak package managers
        - edit apt sources.list
        - edit dnf.conf
    4. install flatpak packages
    5. install gnome extensions
    6. add flatpak repos
    7. add rpmfusion repos
    8. install codecs
    9. install drivers

principles:

    - only use sudo inside script. never run this script as root.
    - use native package manager for CLI apps as possible
    - use flatpak for GUI apps as possible
    - reusability: make functions as possible
    - clear process: nothing should happen if user selects nothing.
    - no bloat: no unnecessary libraries should be installed.
    - don't reinvent the wheel: use existing libraries as possible.
    - no confirmation should be duplicated: use -y option as possible.
    - stability over efficiency

### 1. get system infos

    - get distro name
    - get desktop environment name

### 2. install packages

    -
