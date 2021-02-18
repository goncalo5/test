# This script clones a changeroot environment in the cheapest possible way
set +e
LANG=C

[ $# -ne 2 ] && {
    echo "Usage:"
    echo "$0 <original_chroot> <clone_chroot>"
    exit 1
}

src=$1
dest=$2

if [ ! -d "$1" -o ! -f "$1/var/log/bootstrap.log" ]; then
    echo "Given source \"$1\" is not a changeroot environment, aborting."
    exit 1
fi

if [ -d "$2" ]; then
    if [ -f "$2/var/log/bootstrap.log" ]; then
        echo "Given destination \"$2\" is a changeroot environment, clearing it for you."
        rm -rf $2
    else
        echo "Given destination \"$2\" is a directory but no changeroot environment, aborting."
        exit 1
    fi
fi

HARDLINK_MODE="--reflink=auto"

if [ x"`cp --help | grep -c reflink`" = x"0" ]; then
    echo "--reflink option not yet available to \"cp\", falling back to older approach."
    HARDLINK_MODE=""
fi

mkdir -p $2
res=$?
if [ $res -ne 0 ]; then
    echo "Could not create \"$2\", aborting."
    exit $res
fi

cp --link -aR ${HARDLINK_MODE} -t $2 $1/*
res=$?

exit $res
