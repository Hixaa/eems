# Getting Started
Follow the steps to get started with building the system

## Wiring Diagram
![](images/hardware-diagram.png)

### Wire Details
![](images/wiring.png)

## Raspberry Pi Configuration
Once the system is wired up. 

Note: **Make sure to use Raspbian OS 32 bit Legacy. Latest Raspbian (Bullseye) is not supported by Anydesk**

* Flash the SD card using a fresh Image of Raspbian OS 32 bit (Legacy).
* Enable SSH and WiFi using the advanced settings page.
![](images/os.png)
![](images/settings.png)
* Once the SD card is flashed insert it into the Raspberry Pi and wait for the initial bootup
* Find the IP address of Pi and log into it via SSH
* Clone all the source files from github
```sh
$ sudo apt update
$ sudo apt install git
$ git clone https://github.com/hixaa/eemsV2
```
* Run the install script to install and update all the necessary things using 
```sh
$ cd eemsV2
$ sudo chmod +x install.sh
$ sudo ./install.sh
```
* Enable VNC using `sudo raspi-config`
* Connect with VNC and enable unattended access in Anydesk 
![](images/unattended.png)
* Now you should have the whole system configured, to make the service on boot run
```sh
$ sudo chmod +x onboot.sh
$ sudo ./onboot.sh
```

Now the installation is complete!
