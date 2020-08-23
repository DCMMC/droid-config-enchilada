#!/bin/bash

set -- $(cat /proc/cmdline)
for x in "$@"; do
    case "$x" in
        androidboot.slot_suffix=*)
        ACTIVESLOT="${x#androidboot.slot_suffix=}"
        ;;
    esac
done


# This loop reads every partition in /dev/block/bootdevice/by-name that has an _ in it,
# removes any underscore followed by a single char (e.g. _a, _b) and creates a symlink
# from the 'active slot' partition to one without the slot suffix
# ie if "system_a" is the active partition then "system" will be created so that mounts don't have to care
# about slots.
# Unfortunately this seems to make systemd mount units unhappy as the symlinks weren't created by udev.
echo "Active slot is: $ACTIVESLOT, creating symlinks"
lastPart=""
set -- $(ls /dev/block/bootdevice/by-name/ | grep -e ".*_.*")
for partWithSuffix in "$@"; do
    part=${partWithSuffix%_*} # Substitution to remove the _ and everything after it
    # Every partiton will appear twice so check that we didn't just do this one.
    if [ "$part" != "$lastPart" ]; then
        FROM=$(readlink /dev/block/bootdevice/by-name/$part$ACTIVESLOT)
        TO="/dev/block/bootdevice/by-name/$part" # As only the suffixed ones exist
        CMD="ln -s $FROM $TO"
        echo "$CMD"
        $CMD
        lastPart=$part
    fi
done

function domount() {
    echo "Mounting $WHAT on $WHERE ($TYPE with $OPTIONS)"
    [[ ! -f $WHERE ]] && [[ ! -d $WHERE ]] && mkdir -p $WHERE
    if [ ! -z $OPTIONS ]; then
        mount $WHAT $WHERE -t $TYPE -o $OPTIONS
    else
        mount $WHAT $WHERE -t $TYPE
    fi
    [[ $? -ne 0 ]] && echo "ERROR: Failed to mount $WHAT on $WHERE ($TYPE with $OPTIONS)."
}

mount /dev/block/bootdevice/by-name/system /system_root -o ro,barrier=1,discard
mount --bind /system_root/system /system

mount /dev/block/bootdevice/by-name/vendor /vendor

# Now all the other crap

WHAT=none
WHERE=/config
TYPE=configfs
OPTIONS=
domount
WHAT=cg2_bpf
WHERE=/dev/cg2_bpf
TYPE=cgroup2
OPTIONS=nodev,noexec,nosuid
domount
WHAT=none
WHERE=/dev/cpuctl
TYPE=cgroup
OPTIONS=nodev,noexec,nosuid,cpu
domount
WHAT=none
WHERE=/dev/cpuset
TYPE=cpuset
OPTIONS=nodev,noexec,nosuid
domount
WHAT=none
WHERE=/dev/stune
TYPE=cgroup
OPTIONS=nodev,noexec,nosuid,schedtune
domount
WHAT=bpf
WHERE=/sys/fs/bpf
TYPE=bpf
OPTIONS=nodev,noexec,nosuid
domount
WHAT=/dev/block/bootdevice/by-name/bluetooth
WHERE=/vendor/bt_firmware
TYPE=vfat
OPTIONS=ro,shortname=lower,uid=1002,gid=3002,dmask=227,fmask=337
domount
WHAT=/dev/block/bootdevice/by-name/dsp
WHERE=/vendor/dsp
TYPE=ext4
OPTIONS=ro,nosuid,nodev,barrier=1
domount
WHAT=/system/etc/audio_policy_configuration.xml
WHERE=/vendor/etc/audio/audio_policy_configuration.xml
TYPE=none
OPTIONS=bind
domount
WHAT=/dev/block/bootdevice/by-name/modem
WHERE=/vendor/firmware_mnt
TYPE=vfat
OPTIONS=ro,shortname=lower,uid=0,gid=1000,dmask=227,fmask=337
domount
WHAT=/system/lib64/hw/power.qcom.so
WHERE=/vendor/lib64/hw/power.qcom.so
TYPE=none
OPTIONS=bind
domount


sleep 2
exit 0