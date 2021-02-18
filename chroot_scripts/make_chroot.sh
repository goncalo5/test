#!/bin/bash
# This script installs a Debian chroot with a lot of goodies for Python
# developers and other generally useful things.
# It installs Etch, Lenny, Squeeze, Wheezy, Jessie and Sid in either 32 or 64 bit.
set +e
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

SCRIPT_DIR=$(dirname $0)

FINALIZE_CHROOT=${FINALIZE_CHROOT:-"${SCRIPT_DIR}/finalize_chroot.sh"}
chmod 755  "$FINALIZE_CHROOT"
[ -x "$FINALIZE_CHROOT" ] || {
    echo "finalize_chroot script not found at <$FINALIZE_CHROOT> or not executable" >&2
    exit 1
}

ACTIVATE_CHROOT=${ACTIVATE_CHROOT:-"${SCRIPT_DIR}/activate_chroot.sh"}
[ -x "$ACTIVATE_CHROOT" ] || {
    echo "activate_chroot script not found at <$ACTIVATE_CHROOT> or not executable" >&2
    exit 1
}

BOOTSTRAP_CHROOT=${BOOTSTRAP_CHROOT:-"${SCRIPT_DIR}/bootstrap_chroot.sh"}
[ -x "$BOOTSTRAP_CHROOT" ] || {
    echo "bootstrap_chroot script not found at <$BOOTSTRAP_CHROOT> or not executable" >&2
    exit 1
}

INSTALL_PACKAGES=${INSTALL_PACKAGES:-"${SCRIPT_DIR}/install_packages.sh"}
[ -x "$INSTALL_PACKAGES" ] || {
    echo "install_packages script not found at <$INSTALL_PACKAGES> or not executable" >&2
    exit 1
}

ADD_DEBIAN_MIRROR=${ADD_DEBIAN_MIRROR:-"${SCRIPT_DIR}/add_debian_mirror.sh"}
[ -x "$ADD_DEBIAN_MIRROR" ] || {
    echo "add_debian_mirror script not found at <$ADD_DEBIAN_MIRROR> or not executable" >&2
    exit 1
}

[ "$UID" != "0" ] && {
    echo "You need to be root to run this program" >&2
    syntax
    exit 1
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
mirror="$4"

${BOOTSTRAP_CHROOT} ${arch} ${release} ${target} ${mirror}
RES=$?
[ x"$RES" = x"0" ] || {
    echo "bootstrap script not successful, aborting!" >&2
    exit 1
}

# Do additional setup on the chroot. We start outside the chroot, later
# continue inside the chroot.
echo "Install complete, finalizing the chroot now"

[ "$release" = "buster" ] && chroot $target apt-get install --assume-yes --force-yes "gnupg" "gnupg1-curl"

# lenny is now unsupported and has been moved to the archives.
if [ "$release" = "lenny" ]; then
    ${ADD_DEBIAN_MIRROR} ${target} http://archive.debian.org/debian-archive/debian ${release} "main contrib"
    ${ADD_DEBIAN_MIRROR} ${target} http://archive.debian.org/debian-security ${release}/updates "main contrib"
elif [ "$release" = "squeeze" ]; then
    # As described at https://wiki.debian.org/DebianSqueeze
    ${ADD_DEBIAN_MIRROR} ${target} http://archive.debian.org/debian ${release}
    ${ADD_DEBIAN_MIRROR} ${target} http://archive.debian.org/debian ${release}-lts
    echo "Acquire::Check-Valid-Until false;" > ${target}/etc/apt/apt.conf.d/10allow-archive
else
    ${ADD_DEBIAN_MIRROR} ${target} http://httpredir.debian.org/debian ${release}
    ${ADD_DEBIAN_MIRROR} ${target} http://security.debian.org/ ${release}/updates "main contrib"
fi

if [ "$release" = "jessie" ]; then
    ${ADD_DEBIAN_MIRROR} ${target} http://archive.debian.org/debian jessie-backports "main"
    echo "Acquire::Check-Valid-Until false;" > ${target}/etc/apt/apt.conf.d/10allow-archive
fi

# sourcing packages to be installed: $UTILIITES and $PYTHON_STUFF
source "$SCRIPT_DIR/package_lists"

# Things that did not yet exist in Etch.
[ "$release" != "etch" ] && {
    PYTHON_STUFF="$PYTHON_STUFF python-kerberos python-pexpect"
    # transport-https allows you to use https repositories in /etc/apt/sources.list
    UTILITIES="$UTILITIES iperf python-pyrad trickle iotop arping apt-transport-https"
}
# Lenny comes with Python 2.5, add 2.4 to make Zope happy.
[ "$release" = "lenny" ] && PYTHON_STUFF="$PYTHON_STUFF python2.4"
# Things that were introduced after Lenny.
[ "$release" != "etch" -a "$release" != "lenny" ] && {
    PYTHON_STUFF="$PYTHON_STUFF python-unittest2 python-netaddr"
    UTILITIES="$UTILITIES ca-certificates ngrep dos2unix"
}
# After Debian 8/jessie, mytop is not a Debian package anymore; on 10/buster
# mysql client packages comes from MariaDB
if [ "$release" = "buster" ]; then
    UTILITIES="$UTILITIES default-mysql-client libmariadb-dev-compat"
elif [ "$release" = "stretch" ]; then
    UTILITIES="$UTILITIES mysql-client"
else
    UTILITIES="$UTILITIES mysql-client mytop"
fi

# additionally after Lenny needs to install latest gevent,
# for jessie, this will be done from backport
[ "$release" != "etch" -a "$release" != "lenny" -a "$release" != "jessie" ] && {
    PYTHON_STUFF="$PYTHON_STUFF python-gevent"
}

[ "$release" = "squeeze" ] && PYTHON_STUFF="$PYTHON_STUFF python2.6 python2.5"
# Python is 2.7 by default for Wheezy, add python2.6, python2.5 does not exist
# any more. Jessie has no more python2.6 right now, so don't try to install it.
# Sid has python2.6, but since Jessie doesn't get it, neither should Sid.
[ "$release" = "wheezy" ] && PYTHON_STUFF="$PYTHON_STUFF python2.6"

# This will also install security updates.
${INSTALL_PACKAGES} ${target} "${UTILITIES} ${PYTHON_STUFF}"

# jessie must install gevent from backport
[ "$release" = "jessie" ]  && chroot $target apt-get install --assume-yes --force-yes -t jessie-backports "python-gevent"

# In Wheezy and earlier, Midnight Commander will not start without this symlink.
# It is not needed in Jessie.
if [ "$release" = "etch" -o "$release" = "lenny" -o "$release" = "squeeze" -o "$release" = "wheezy" ]; then
    ln -s /usr/share/mc/bin/mc-wrapper.sh $target/usr/share/mc/mc-wrapper.sh
fi

${ACTIVATE_CHROOT} ${target}
${FINALIZE_CHROOT} ${target}

