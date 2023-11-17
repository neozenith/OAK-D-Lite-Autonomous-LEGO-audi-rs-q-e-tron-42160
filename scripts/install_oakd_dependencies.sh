#! /bin/bash
# Adapted from sudo curl -fL https://docs.luxonis.com/install_dependencies.sh | bash
sudo apt-get update
sudo apt-get upgrade -y
python3 -m pip install -U pip
sudo apt-get install -y \
    python3 \
    python3-pip \
    udev \
    cmake \
    git \
    python3-numpy \
    build-essential \
    libgtk2.0-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    python3-dev \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1-mesa-glx \
    python3-pyqt5 \
    python3-pyqt5.qtquick \
    qml-module-qtquick-controls2 \
    qml-module-qt-labs-platform \
    qtdeclarative5-dev \
    qml-module-qtquick2 \
    qtbase5-dev \
    qtchooser \
    qt5-qmake \
    qtbase5-dev-tools \
    qml-module-qtquick-layouts \
    qml-module-qtquick-window2 

echo "Installing udev rules..."
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules > /dev/null
sudo udevadm control --reload-rules && sudo udevadm trigger