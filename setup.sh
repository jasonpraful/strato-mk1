#!/bin/bash

# This script is used to build the project.


mkdir ~/strato
mkdir ~/strato/logs


# installing python and pip
sudo apt-get install python3-pip python3-dev 
clear

# Installing Sensor Dependencies
echo 'Installing dependencies'

#BMP Weather
sudo pip3 install adafruit-circuitpython-bmp280
#BH Light sensor
sudo pip3 install adafruit-circuitpython-bh1750

sudo pip3 install pynmea2



sudo echo -e "dtparam=spi=on\ndtoverlay=pi3-disable-bt\ncore_freq=250\nenable_uart=1\nforce_turbo=1" >> /boot/config.txt

sudo cp /boot/cmdline.txt /boot/cmdline_backup.txt

sudo echo -e "dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles" >> /boot/cmdline.txt

sudo systemctl stop serial-getty@ttyAMA0.service
sudo systemctl disable serial-getty@ttyAMA0.service
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service





# Reboot after everything is done
echo 'Rebooting'
sudo reboot
