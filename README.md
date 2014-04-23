#PiTrackCam

I've got a Raspberry Pi that walks down a tracking taking pictures.
If your Raspberry Pi GPIO diagram doesn't have GPIO27 you need to find a new diagram.
This is how I built it.

## Get Hardware

* Buy a Raspberry Pi
* Buy a Raspberry Pi Camera Module
* Buy a dirt cheap 4-pin 5V stepper with driver on eBay.
  * 28YBJ-48
* Make sure you have an SD card to install Raspbian on
* Find an old USB flash drive and format it Fat32.

## Configure Hardware

* Connect camera module
* Connect SD card
* Connect flash drive
* Connect stepper to driver (if not already done)
* Connect driver power to Pi
  * Driver pin [+] to Pi pin [2] (5VDC)
  * Driver pin [-] to Pi pin [6] (GND)
* Connect driver signal to Pi
  * Driver pin [IN1] to Pi pin [11] (GPIO 17)
  * Driver pin [IN2] to Pi pin [13] (GPIO 27)
  * Driver pin [IN3] to Pi pin [15] (GPIO 22)
  * Driver pin [IN4] to Pi pin [16] (GPIO 23)

## Get Software

* Install Raspbian
* Using Initial Config Screen
  * Expand the File System
  * Enable Camera Support
* Localize the System
```
sudo dpkg-reconfigure keyboard-configuration
```
* Remove Unused Stuff
```
sudo apt-get –purge remove scratch wolfram-engine
sudo apt-get autoremove –purge
```
* Add Python Camera and Python Imaging Support
```
sudo apt-get install python-picamera python-imaging
```
* Clone this Repo
```
git clone https://github.com/jimlind/PiTrackCam.git
```

## Configure Software

* Edit your _etc/rc.local_ file and place the following before the 'exit 0'
```
#Autorun PiTrackCam
/home/pi/PiTrackCam/starwork.sh
```
