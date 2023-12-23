import subprocess


def setup():
    subprocess.run("python3 -m venv venv", shell=True)
    subprocess.run("source venv/bin/activate", shell=True)
    subprocess.run("venv/bin/pip3 install -r requirements.txt", shell=True)
