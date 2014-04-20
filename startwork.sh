#!/bin/sh

mountpath="/media/USB"

# Try to create folder to mount USB drive to
# Hide errors
mkdir -p $mountpath 2> /dev/null

# Find available drive
# Hide errors
path=$(find /sys/block/sd* 2> /dev/null | head -1 )
drive=${path##*/}

if [ -z "$drive" ]
then
    echo "Not able to find a worthwhile drive."
    exit 0
fi

echo "Mounting $drive to $mountpath"
mount -t vfat /dev/${drive}1 $mountpath

exit 0

python /home/pi/capture/work.py
