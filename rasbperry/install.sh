#!/bin/bash

sudo apt-get install -y git \
    python3 

# https://github.com/Pioreactor/rpi_hardware_pwm
pip3 install rpi-hardware-pwm --break-system-packages
pip3 install websockets --break-system-packages
# pip3 install dataclasses-json --break-system-packages
# sudo nano /boot/firmware/config.txt

# TODO: Uncomment
#sudo bash -c 'echo "dtoverlay=pwm-2chan,pin=12,func=4,pin2=13,func2=4" >> /boot/firmware/config.txt'

# Get the current kernel version
current_kernel=$(uname -r)

# https://github.com/Pioreactor/rpi_hardware_pwm/issues/14
if [[ "$current_kernel" == "6.6.20+rpt-rpi-2712" ]]; then
  sudo apt install raspberrypi-kernel
  echo "Kernel version matches! Installing raspberrypi-kernel..."
else
  echo "Kernel version does not match (current: $current_kernel)"
fi

sudo reboot now