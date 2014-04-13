#!/usr/bin/python

from picamera import PiCamera

import time as Time
import Image
import ImageOps

width   = 1920
height  = 1080

camera = PiCamera()
Time.sleep(1)

camera.resolution = (width, height)
camera.awb_mode = 'off'
camera.ISO = 800
camera.shutter_speed = 5000
camera.brightness = 50
camera.contrast = 0
camera.led = False
Time.sleep(60)

camera.capture('/home/pi/capture/low.jpg', use_video_port=True)

Time.sleep(1)

camera.resolution = (2592, 1944)

Time.sleep(60)

camera.capture('/home/pi/capture/high.jpg', use_video_port=True)

im = Image.open('/home/pi/capture/high.jpg')
smaller = ImageOps.fit(im, (1920, 1080), Image.ANTIALIAS, (0.5, 0.5))
smaller.save('/home/pi/capture/high-small.jpg', 'JPEG', quality=95)



camera.close()
