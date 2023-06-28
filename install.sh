#!/bin/bash

echo "[+] Starting Debloat\n"

# Remove bloatware
sudo apt remove --purge wolfram-engine libreoffice* scratch* minecraft-pi sonic-pi dillo gpicview oracle-java8-jdk openjdk-7-jre oracle-java7-jdk openjdk-8-jre vlc chromium-browser geany thonny piclone qpdfview rpi-imager mousepad galculator gpicview rp-bookshelf debian-reference-common -y

# autoremove
sudo apt autoremove -y

# clean
sudo apt autoclean -y

echo "[+] Performing system upgrade\n"
# update
sudo apt update
sudo apt upgrade


echo "[+] Installing anydesk\n"
# install anydesk
sudo apt install libminizip1 libegl1-mesa
sudo apt install libgles-dev libegl-dev
sudo ln -s /usr/lib/arm-linux-gnueabihf/libGLESv2.so /usr/lib/libbrcmGLESv2.so
sudo ln -s /usr/lib/arm-linux-gnueabihf/libEGL.so /usr/lib/libbrcmEGL.so
sudo ldconfig
sudo apt install ./tools/anydesk_6.1.1-1_armhf.deb

echo "[+] Installing scripts\n"
sudo apt install vim
pip3 install urllib3
pip3 install requests
pip3 install chardet
sudo mv ./xaees/xaees.service /lib/systemd/system/
sudo cp -r ./xaees/* /

echo "[+] Done with the installation\n"
echo "[*] Please do a REBOOT\n"
