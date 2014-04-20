#!/usr/bin/python

from picamera import PiCamera

import Image
import ImageOps
import time as Time

class Camera:
    max_size = (2592, 1944)
    normal_size = (1920, 1080)

    camera = None

    def set_settings(self, optimal):
        camera = PiCamera()
        Time.sleep(1)

        camera.resolution = self.max_size
        camera.awb_mode = 'off'
        camera.ISO = optimal['iso']
        camera.shutter_speed = optimal['ss']
        camera.brightness = 50
        camera.contrast = 0
        camera.led = False
        Time.sleep(60)

        self.camera = camera

    def snap(self, file):
        self.camera.capture(file, use_video_port=True)
        Time.sleep(0.1)

        im = Image.open(file)
        smaller = ImageOps.fit(im, self.normal_size, Image.ANTIALIAS, (0.5, 0.5))
        smaller.save(file, 'JPEG', quality=98)
