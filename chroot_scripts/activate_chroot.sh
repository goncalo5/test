#!/bin/bash
# This script activates a chroot, i.e. makes it usable for e.g. processes
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

[ ! -d "$target/proc" -o ! -d "$target/dev/pts" ] && {
    echo "Directories \"$target/proc\" and \"$target/dev/pts\" need to exist!" 1>&2
    exit 1
}

# Take some config from the host system because the chroot has no way of
# knowing about this stuff:
cp /etc/hosts "$target/etc/hosts"
cp /etc/resolv.conf "$target/etc/resolv.conf"


# Name of the chroot appears in prompt with green color, kindly done by
# /etc/bash.bashrc. We put the directory name of the chroot in there, e.g.
# if the chroot was installed in /opt/production_axess, the prompt will be
# (production_axess) root@hostname:/#
chroot_name=`basename "$target"`
echo "$chroot_name" > "$target/etc/debian_chroot"

# Python complains (at least on Squeeze, Wheezy, Jessie) if this directory
# does not exist.
mkdir -p "$target/etc/pythonstart"

mount -o bind /proc "$target/proc"
mount -o bind /dev/pts "$target/dev/pts"
if grep ^7 "$target/etc/debian_version"; then
    # Only Wheezy: /dev/shm is a symlink to /run/shm
    mount -o bind /dev/shm "$target/run/shm"
else
    # Squeeze and earlier, also Jessie.
    mount -o bind /dev/shm "$target/dev/shm"
fi

