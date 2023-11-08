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


