#!/bin/sh

mkdir /media/USB

drive=$(find /sys/block/sd* | head -1)
echo "$drive"

echo ${drive##>*/}

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
