#PiTrackCam

I've got a Raspberry Pi that walks down a tracking taking pictures.
This is how I built it.

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
* Add Python Camera Support
```
sudo apt-get install python3-picamera
```
* Clone this Repo
```
git clone https://github.com/jimlind/PiTrackCam.git
```