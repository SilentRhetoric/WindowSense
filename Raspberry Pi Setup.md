# Setting Up Your Raspberry Pi

## Hardware Build



## Headless Access

The following instructions cover how to prepare a "headless" Raspberry Pi (no 
monitor) to run WindowSense and be accessible remotely via SSH and/or VNC Viewer.

### Preparing the SD Card



### To connect via SSH

- Set the Host Name (or IP address) field to raspberrypi.local
- By default the Port should be set to 22 and Connection type should be set to SSH
- Click Open
- If you see a Security Alert select Yes
- A new terminal window should appear prompting you for a user name
- The default user name is `pi`
- The default password is `raspberry`

### To enable VNC (should also change hostname & password)  

`sudo raspi-config`

To edit config.txt:  
`sudo nano /boot/config.txt`

To get updates:  
`sudo apt update -y`
`sudo apt upgrade -y`

### Wifi Setup
To edit or review your wifi settings, run this command

`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

This command should list your network in the first line for wlan0:  
`iwconfig`

This command should show info for wlan0:  
`ifconfig`

This command should list your network name:  
`iwlist wlan0 scan | grep ESSID`

### To update python alternatives  

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
