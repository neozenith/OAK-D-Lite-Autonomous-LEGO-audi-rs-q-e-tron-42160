# OAK-D-Lite-Autonomous-LEGO-audi-rs-q-e-tron-42160

Lego Autonomous Vehicle Build Audi RS Q e-tron 42160 using an OAK-D Lite Neural Camera and RaspberryPi 4B with PiJuice. https://www.lego.com/en-au/product/audi-rs-q-e-tron-42160

## Raspberry Pi Setup

### Setup VNC Viewer

Enable VNC Server:

```sh
sudo apt-get update && sudo apt-get upgrade -y
sudo raspi-config
# Use keyboard to enable VNC ports
```

Install VNC Viewer Desktop tool:

```sh
sudo apt install realvnc-vnc-server realvnc-vnc-viewer -y
```

## OAK-D Lite Setup

https://docs.luxonis.com/projects/hardware/en/latest/pages/guides/raspberrypi/

```sh
# sudo curl -fL https://docs.luxonis.com/install_dependencies.sh | bash

# Ported a simplified working version of the above
. ./scripts/install_dependencies.sh
```

```sh
python3 -m venv .venv
. ./.venv/bin/activate
python3 -m pip install depthai
```

```sh
git clone https://github.com/luxonis/depthai-python.git
cd depthai-python
```
