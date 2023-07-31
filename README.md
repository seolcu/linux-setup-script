# linux_setup_script

initial setup script for some distros.

## setup

### 1. clone this repo

```bash
sudo apt install git
git clone https://github.com/seolcu/linux_setup_script
cd linux_setup_script
```

### 2. setup python venv

```bash
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r pip_requirement.txt
```

### 3. execute the script

```bash
./setup.py
```

### 4. cleanup

```bash
deactivate
cd ..
rm -rf linux_setup_script
```
