#!/bin/bash
# This script deactivates a chroot, i.e. makes it unusable for e.g. processes
set +e
LANG=C

[ $# != 1 ] && {
    echo "Need an chroot directory as argument" 1>&2
    exit 1
}

[ $UID != 0 ] && {
    echo "You need to be root to run this program" 1>&2
    exit 1
}

target="$1"

[ -d "$target/proc"  ] && {
    umount "$target/proc"
}

[ -d "$target/dev/pts" ] && {
    umount "$target/dev/pts"
}

# Squeeze and earlier, also Jessie.
mountpoint="$target/dev/shm"
[ -d "$mountpoint" ] && {
    umount "$mountpoint"
}

# Only in Wheezy: /dev/shm is a symlink to /run/shm
mountpoint="$target/run/shm"
[ -d "$mountpoint" ] && {
    umount "$mountpoint"
}

exit 0
