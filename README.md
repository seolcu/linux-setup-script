# linux-setup-script

initial setup script for some distros.

## setup

### 1. clone this repo

```bash
sudo apt install git
git clone https://github.com/seolcu/linux-setup-script
cd linux-setup-script
```

### 2. setup python venv

```bash
sudo apt install python3-venv
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
