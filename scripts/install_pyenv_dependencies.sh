#! /bin/bash
# Install dependencies required to build new versions of Python from PyEnv
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libgdbm-dev \
    lzma \
    lzma-dev \
    tcl-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    wget \
    curl \
    make \
    build-essential \
    openssl