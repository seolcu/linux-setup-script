# linux-setup-script

OOTB productive setup script for [debian, arch, nix], GNOME.

## setup

### 0. prerequisites

- python3-venv
- git

### 1. clone this repo

```bash
git clone https://github.com/seolcu/linux-setup-script
cd linux-setup-script
```

### 2. setup venv

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
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

- this script is not using gext anymore, so you should install gnome extensions manually if they are not provided by official repos.
