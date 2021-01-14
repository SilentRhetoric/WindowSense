# Setting Up A Headless Raspberry Pi
This is not a complete guide to getting a headless Pi Zero set up from scratch, but it is 
a collection of my personal notes and links which cover the vast majority of the configuration required to do so.

#### Preparing the SD Card
Download the [Raspberry Pi OS Imager](https://www.raspberrypi.org/software/) to be able to flash
your preferred build of the OS onto a Micro SD card.

##### Headless Setup
[Setting Up A Raspberry Pi headless](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) from Raspberry Pi's documentation.

#### Remote Access Options
[Remote Access](https://www.raspberrypi.org/documentation/remote-access/README.md) from Raspberry Pi's documentation.

#### To connect via SSH

- Set the Host Name (or IP address) field to raspberrypi.local
- By default the Port should be set to 22 and Connection type should be set to SSH
- Click Open; if you see a Security Alert select Yes
- A new terminal window should appear prompting you for a user name
- The default user name is `pi`
- The default password is `raspberry`

To enable VNC (should also change hostname & password)  
[Virtual Network Computing](https://www.raspberrypi.org/documentation/remote-access/vnc/) from Raspberry Pi's documentation.

[VNC Connect and Raspberry Pi](https://help.realvnc.com/hc/en-us/articles/360002249917-VNC-Connect-and-Raspberry-Pi) from RealVNC's documentation.

`sudo raspi-config`

To edit config.txt:  
`sudo nano /boot/config.txt`

To get updates:  
`sudo apt update -y`
`sudo apt upgrade -y`

#### Wifi Settings
To edit or review your wifi settings, run this command

`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

This command should list your network in the first line for wlan0:  
`iwconfig`

This command should show info for wlan0:  
`ifconfig`

This command should list your network name:  
`iwlist wlan0 scan | grep ESSID`

#### To update python alternatives  

Raspberry Valley provides a helpful guide to configuring the default version of 
Python which your Pi uses:  
[Configure Default Python version on your Pi](<https://raspberry-valley.azurewebsites.net/Python-Default-Version/>)

To check versions:  
`python --version`  
`python3 --version`

To show the list of alternatives:  
`sudo update-alternatives --list python`  

To update the alternatives and priorities:  `sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1`  
`sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2`  

To remove a version from the alternatives:  
`sudo update-alternatives --remove python /usr/bin/python3.5`  
