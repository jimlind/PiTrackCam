# Import required libraries
from lib.camera   import Camera
from lib.settings import Settings
from math         import ceil
from os           import listdir as list_dir
from os           import mkdir   as make_dir
from os.path      import exists  as path_exists
from os.path      import ismount as is_path_mount
from sys          import argv    as arguments
from sys          import exit    as system_exit

import RPi.GPIO as PinIO
import time     as Time

# Default configuration
cycles_per_photo = 5
stepper_wait = 0.010
photo_wait = 5

# Check arguments
if len(arguments) !== 2:
    print 'Incorrect agrument count. Must include location.'
    system_exit(0)

# Make sure a drive is mounted
external_USB = arguments[1]
if not is_path_mount(external_USB):
    print external_USB
    print 'Location is not a mounted drive.'
    system_exit(0)

# Make sure saving folder exists
frames_dir = external_USB + '/frames'
if (not path_exists(frames_dir)):
    make_dir(frames_dir, 0777)

# Use BCM GPIO references instead of physical pin numbers
PinIO.setwarnings(False)
PinIO.setmode(PinIO.BCM)

# Define GPIO signals to use
# Pins [11, 12, 13, 15] => [GPIO17, GPIO18, GPI21, GPI22]
step_pins = [17,18,27,22]

# Set all pins as output
for pin in step_pins:
    PinIO.setup(pin, PinIO.OUT)
    PinIO.output(pin, False)

# Define counters
step_counter = 0
cycle_counter = 0

# Define stepper sequence
sequence = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1],
]

# Find best camera settings
settings = Settings()
auto_settings = settings.get_auto()

# Find closest allowed ISO
speed = auto_settings['iso']
speeds = [100, 200, 320, 400, 500, 640, 800]
iso = 800
minimum_diff = float('inf')
for value in speeds:
    diff = abs(speed - value)
    if diff <= minimum_diff:
        minimum_diff = diff
        iso = value
auto_settings['iso'] = iso

# Setup camera for capture
camera = Camera()
camera.set_settings(auto_settings)
photo_counter = 0

# Check for previous folders
for content in list_dir(frames_dir):
    if path_exists(frames_dir + '/' + content):
        folder_number = (int(content) + 1) * 1000
        if folder_number > photo_counter:
            photo_counter = folder_number

# Start main loop
while 1==1:
    # Set pins for next stepper motor
    for index in range(0, 4):
        pin = step_pins[index]
        if sequence[step_counter][index] != 0:
            PinIO.output(pin, True)
        else:
            PinIO.output(pin, False)

    # Next step
    step_counter += 1

    # If we reach the end of the sequence, start again
    if (step_counter == 8):
        step_counter = 0

    # Wait before moving on
    Time.sleep(stepper_wait)

    # Advance cycle counter when step counter resets
    if (step_counter == 0):
        cycle_counter += 1

    # Take photo based on cycle counter
    if (cycle_counter == cycles_per_photo):
        # Make sure saving folder exists
        sub_folder = frames_dir + '/' + str(int(ceil(photo_counter / 1000)))
        if (not path_exists(sub_folder)):
            make_dir(sub_folder, 0777)

        # Wait and snap
        Time.sleep(photo_wait)
        camera.snap(sub_folder + '/' + str(photo_counter) + '.jpg')

        # Next
        cycle_counter = 0
        photo_counter += 1
