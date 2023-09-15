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

### what this script do:

1. system setup
   - fwupdmgr: firmware update(no -y option!! must be confirmed by user)
   - keyboard faulty fn keys fix
2. native package management
   - tweak native package managers
   - edit repos
   - update packages
   - install codecs and drivers
   - install native packages
   - remove unnecessary packages
3. flatpak management
   - setup flatpak
   - install flatpak packages
   - add flatpak repos
4. desktop environment setup
   - install extensions
5. etc

### principles:

- only use sudo inside script. never run this script as root.
- use native package manager for CLI apps as possible
- use flatpak for GUI apps as possible
- reusability: make functions as possible
- clear process: nothing should happen if user selects nothing.
- no bloat: no unnecessary libraries should be installed.
- don't reinvent the wheel: use existing libraries as possible.
- no confirmation should be duplicated: use -y option as possible.
- stability over efficiency
