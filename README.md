# linux-setup-script

OOTB productive setup script for [debian, arch, fedora, nix], GNOME.

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

## Suggested GNOME Extensions (From GNOME Extensions Website)

- [AppIndicator and KStatusNotifierItem Support](https://extensions.gnome.org/extension/615/appindicator-support/) (Requires `libappindicator`)
- [GSConnect](https://extensions.gnome.org/extension/1319/gsconnect/) ([Optional features requires additional packages](https://github.com/GSConnect/gnome-shell-extension-gsconnect/wiki/Installation#optional-features))
- [Caffeine](https://extensions.gnome.org/extension/517/caffeine/)
- [Vitals](https://extensions.gnome.org/extension/1460/vitals/) (Requires [Supporting Packages](https://github.com/corecoding/Vitals?tab=readme-ov-file#1-install-support-packages))
- [Thinkpad Battery Threshold](https://extensions.gnome.org/extension/4798/thinkpad-battery-threshold/)
