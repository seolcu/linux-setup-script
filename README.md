# linux-setup-script

initial setup script for some distros.
currently support Debian/Fedora/Mint, GNOME/KDE/Cinnamon/Xfce.

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

### what this script do:

1. system setup
   1. fwupdmgr: firmware update(no -y option!! must be confirmed by user)
   2. keyboard faulty fn keys fix
2. native package management
   1. tweak native package managers
   2. edit repos
   3. update packages
   4. install codecs and drivers
   5. install native packages
   6. remove unnecessary packages
3. flatpak management
   1. setup flatpak
   2. add flatpak repos
   3. install flatpak packages
4. desktop environment setup
   1. install extensions
5. etc

### principles:

- only use sudo inside script. never run this script as root.
- use native package manager for CLI apps as possible
- use flatpak for GUI apps as possible
- reusability: make functions as possible
- no bloat: no unnecessary libraries should be installed.
- don't reinvent the wheel: use existing libraries as possible.
- clear process: nothing should happen if user selects nothing.
- always ask for confirmation
- no confirmation should be duplicated
- stability over efficiency
- Keep it simple: no unnecessary features.

### todos:

- add 'up' command to simplify update process
