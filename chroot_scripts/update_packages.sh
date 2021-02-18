# This script updates all installed packages within a changeroot
set +e
LANG=C

[ $# -ne 1 ] && {
    echo "Usage:"
    echo "$0 <chroot>"
    exit 1
}

target=$1

if [ ! -d "$1" -o ! -f "$1/var/log/bootstrap.log" ]; then
    echo "Given source \"$1\" is not a changeroot environment, aborting."
    exit 1
fi

chroot $target apt-get update
chroot $target apt-get update --no-install-recommends --assume-yes --force-yes

exit 0

