# linux-setup-script

OOTB productive setup script for Debian, GNOME.

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

### 4. cleanup if not needed anymore

```bash
deactivate
cd ..
rm -rf linux-setup-script
```

### notes

- this script is not using gext anymore, so you should install gnome extensions manually if they are not provided by debian.

## documentation: developer manual

### what this script do:

1. apt management
   1. tweak native package managers
   2. update packages
   3. install native packages
2. flatpak management
   1. install flatpak
   2. add flatpak repos
   3. install flatpak packages
3. misc
   1. enable firefox on wayland
   2. fix keyboard faulty fn keys
   3. fwupdmgr: firmware update(no -y option!! must be confirmed by user)

### todos:
