# linux-setup-script

initial setup script for some distros.
currently support Debian/Fedora, GNOME.

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

### 4. cleanup

```bash
deactivate
cd ..
rm -rf linux-setup-script
```
