#!/bin/sh

mountpath = "/media/USB"

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
mount /dev/$drives $mountpath

exit 0

for drive in /sys/block/sd*
do
    if readlink $drive/device | grep -q usb
    then
        DEV=`basename $DEV`
        echo "$DEV is a USB device, info:"
        udevinfo --query=all --name $DEV
        if [ -d /sys/block/${DEV}/${DEV}1 ]
        then
            echo "Has partitions " /sys/block/$DEV/$DEV[0-9]*
        else
            echo "Has no partitions"
        fi
        echo "No pants"
    fi
done

exit 0

python /home/pi/capture/work.py
