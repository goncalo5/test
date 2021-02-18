# This script adds a Debian mirror to the chroot
set +e
LANG=C

[ $# -lt 3 ] && {
    echo "Usage:"
    echo "$0 <chroot> <mirror> <distribution> [types]"
    exit 1
}

target=$1
mirror=$2
release=$3
types=${4:-"main"}

full_line="deb ${mirror} ${release} ${types}"

if grep -Fxq "${full_line}" ${target}/etc/apt/sources.list
then
    echo "${full_line} already present"
else
    echo "${full_line}" >> ${target}/etc/apt/sources.list
fi

exit 0
