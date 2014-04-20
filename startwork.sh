#!/bin/sh

mountpath="/media/USB"

# Try to create folder to mount USB drive to
# Hide errors
mkdir -p $mountpath 2> /dev/null

# Find available drive
# Hide errors
path="$(find /sys/block/sd* 2> /dev/null | head -1 )"
drive=${path##*/}

# Exit if no drives available
if [ -z "$drive" ]
then
    echo "Not able to find a worthwhile drive."
    exit 0
fi

# Attempt mounting drive
# Hide errors
echo "Mounting $drive to $mountpath"
mount -t vfat -o uid=pi,gid=pi /dev/${drive}1 $mountpath 2> /dev/null

mountresults="$(mountpoint $mountpath )"
if [ "$mountresults" != "$mountpath is a mountpoint" ]
then
    echo "Not able to mount the drive"
    exit 0
fi

python work.py $mountpath
