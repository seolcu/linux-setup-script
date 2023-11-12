# linux-setup-script

OOTB productive setup script for Fedora, GNOME.

## setup

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

- this script is not using gext anymore, so you should install gnome extensions manually if they are not provided by fedora repos.

## documentation: developer manual

### what this script do:

1. dnf management
   1. update packages
   2. add RPMFusion repos
   3. install neccessary RPMFusion packages (NVIDIA/AMD/Intel)
   4. install native packages
2. flatpak management
   1. install flatpak packages
3. misc
   1. fix keyboard faulty fn keys
   2. fwupdmgr: firmware update(no -y option!! must be confirmed by user)

### todos:
