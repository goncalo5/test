#!/bin/bash
# This script installs a Debian chroot with a lot of goodies for Python
# developers and other generally useful things.
# It installs  Lenny, Squeeze, Wheezy, Jessie, Stretch  and Sid in either 32 or 64 bit.
LANG=C

syntax() {
    echo "Usage: $0 (i386|amd64) (lenny|squeeze|wheezy|jessie|stretch|buster|sid) <chroot directory> [remote|local|<HTTP debian mirror>]"
    echo -e "\tIf \"local\" is passed, artifacts-internal.axiros.com will be used as HTTP server."
    echo -e "\tIf \"remote\" is passed or the parameter is omitted, httpredir.debian.org will be used."
    echo -e "\tIf a custom HTTP URL is passed, this one will be used as mirror."
    exit 1
}

not_in() {
    name=${1}
    shift

    for i in "${@}"; do
        if [ ${name} = ${i} ]; then
            # This signals error => The value is in.
            return 1
        fi
    done

    # This signals 'success' => The value is not in.
    return 0
}

# Normal mode, do sanity checks on arguments
[ -z $3 ] && syntax
not_in ${1} "i386" "amd64" && syntax
not_in ${2} "lenny" "squeeze" "wheezy" "jessie" "stretch" "buster" "sid" && syntax
mkdir -p "$3"
[ -d "$3" ] || syntax
arch="$1"
release="$2"
target="$3"

[ -f "${target}/var/log/bootstrap.log" ] && {
    echo "Bootstrap was already executed before, exiting." >&2
    exit 0
}

[ "$UID" != "0" ] && {
    echo "You need to be root to run this program" >&2
    syntax
    exit 1
}

[ -z "$4" ] && four="remote" || four="$4"
[ "$four" = "local" -o "$four" = "remote" -o "${four:0:4}" = "http" ] || syntax
[ "$four" = "local" -a "$release" = "etch" ] && {
    echo "NOTE: There is no local mirror for Debian Etch" >&2
    echo "NOTE: A remote mirror will be used instead" >&2
    four="remote"
}
[ "$four" = "local" -a "$release" = "lenny" ] && {
    echo "NOTE: There is no local mirror for Debian Lenny" >&2
    echo "NOTE: A remote mirror will be used instead" >&2
    four="remote"
}
[ "$four" = "local" -a "$release" = "squeeze" ] && {
    echo "NOTE: There is no local mirror for Debian Squeeze" >&2
    echo "NOTE: A remote mirror will be used instead" >&2
    four="remote"
}

if [ "${four:0:4}" = "http" ]; then
    mirror=$four
fi
if [ "$four" = "local" ]; then
	mirror="http://artifacts-internal.axiros.com/artifactory/DebianMirror"
fi
if [ "$four" = "remote" ]; then
    if [ "$release" = "lenny" -o  "$release" = "squeeze" ]; then
        mirror="http://archive.debian.org/debian"
    else
        mirror="http://httpredir.debian.org/debian"
    fi
fi

# debootstrap hides in /usr/sbin, which may not be in $PATH.
PATH="$PATH:/usr/sbin"
which debootstrap 2>/dev/null >/dev/null || {
    echo "$0: no debootstrap found in your path."
    exit 2
}

# Start package installation and mount virtual file systems.
debootstrap --arch $arch $release "$target" "$mirror"

# Clean package residue
chroot "$target" apt-get clean

exit
