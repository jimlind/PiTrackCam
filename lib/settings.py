#!/usr/bin/python

from os import remove as rm
from os import system as cmd
from uuid import uuid4

import Image
import tempfile as Temp

class Settings:

    command_prefix = 'raspistill -sh 0 -co 0 -br 50 -sa 0 -ev 0 -ifx none -t 1000 -w 400 -h 400 -n'
    storage = '/tmp/'

    def __init__():
        self.storage = Temp.gettempdir()

    def get_auto(self):
        uuid = str(uuid4())
        file_name = self.storage + uuid + '.jpg'
        command = self.command_prefix + ' -o ' + file_name
        cmd(command)

        im = Image.open(file_name)
        exif_data = im._getexif()
        auto_histogram = im.histogram()

        iso_value = 800
        ss_value = 200000

        maker_notes = exif_data[37500]
        maker_notes_list = maker_notes.split(' ')
        for note in maker_notes_list:
            data = note.split('=')
            key = data[0]
            if key == 'exp':
                ss_value = int((float(data[1]) / 1e6) * 1000000)
            elif data[0] == 'ag':
                iso_value = int(float(data[1]) / 2.56)

        rm(file_name)

        return {
            'iso': iso_value,
            'ss' : ss_value,
        }
