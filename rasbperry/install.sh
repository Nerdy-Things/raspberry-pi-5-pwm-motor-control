# sudo apt install raspberrypi-kernel 

sudo apt-get install -y git \
    python3 

# https://github.com/Pioreactor/rpi_hardware_pwm
pip3 install rpi-hardware-pwm --break-system-packages
pip3 install websockets --break-system-packages
# pip3 install dataclasses-json --break-system-packages
# sudo nano /boot/firmware/config.txt

sudo bash -c 'echo "dtoverlay=pwm-2chan,pin=12,func=4,pin2=13,func2=4" >> /boot/firmware/config.txt'
sudo reboot now