#!/bin/bash

# Script to create a "Mobile Repository"

# You need to provide a package/multiple packages that the repository should
# contain, plus a chroot to build against.

# The Mobile Repository is a software source from which apt-get can install.
# The packages named in this program's parameter will be part of this
# repository, including all dependencies that they require. However,
# dependencies are not included if they were already present in the chroot
# for which the repository was built.
# For example, if a package requires bzip2 and the given chroot did not have
# bzip2 installed, the bzip2 package will be part of the Mobile Repository. If
# the chroot already had bzip2, the Mobile Repository will not contain the
# bzip2 package.

syntax() {
    echo "Usage: $0 <chroot> <repo name> package1 [package2 [package3 ...]]"
    echo -e "\t<chroot>\t\talready existing chroot"
    echo -e "\t<repo name>\t\tfile name of the mobile repo"
    echo -e "\t<package>\t\tPackages to include in the repo. Theses can be either"
    echo -e '\t\t\t\t- local file names, e.g. "/tmp/axiros_whatever.deb"'
    echo -e '\t\t\t\t- package names to install via apt-get, e.g. "mysql-server"'
    exit 1
}

[ $# -lt 3 ] && syntax
NUM_ARGS=$#
MYSELF="$0"
CHROOT="$1"
REPO_NAME="$2"
shift 2
PACKAGES="$*"

COMPRESSOR="gzip"
COMP_EXT="tar.gz"

[ "$UID" != "0" ] && {
    echo "You need to be root to run this program" >&2
    exit 1
}
if [ -z `which reprepro 2>/dev/null` ]; then
    echo "You need to install reprepro" >&2
    exit 1
fi

# Sanity checks on arguments
[ ! -d "$CHROOT" ] && syntax
[ -z "$PACKAGES" ] && syntax

# Go through the packages and check which ones exist on disk
# and which are just names to be loaded from a repo.
PACKAGES_FILES=""
PACKAGES_NAMES=""
for package in $PACKAGES; do
    if [ -f "$package" ]; then
        echo "<$package> is interpreted as file to install."
        PACKAGES_FILES="$PACKAGES_FILES $package"
    else
        echo "<$package> is interpreted as a name"
        PACKAGES_NAMES="$PACKAGES_NAMES $package"
    fi
done

# Figure out which Debian version the chroot is
if grep -q '^8.' "$CHROOT/etc/debian_version"; then
    CHROOT_VERSION="jessie"
    CHROOT_VERSION_NUMBER="8.0"
elif grep -q '^7.' "$CHROOT/etc/debian_version"; then
    CHROOT_VERSION="wheezy"
    CHROOT_VERSION_NUMBER="7.0"
elif grep -q '^6.0' "$CHROOT/etc/debian_version"; then
    CHROOT_VERSION="squeeze"
    CHROOT_VERSION_NUMBER="6.0"
elif grep -q '^5.0' "$CHROOT/etc/debian_version"; then
    CHROOT_VERSION="lenny"
    CHROOT_VERSION_NUMBER="5.0"
elif grep -q '^4.0' "$CHROOT/etc/debian_version"; then
    CHROOT_VERSION="etch";
    CHROOT_VERSION_NUMBER="4.0"
else
    echo "Could not determine the chroot's Debian version. Aborting." 1>&2
    exit 1
fi
# Figure out the architecture
if `chroot "$CHROOT" file /bin/bash | grep -q "32-bit"`; then
    CHROOT_ARCH="i386"
elif `chroot "$CHROOT" file /bin/bash | grep -q "64-bit"`; then
    CHROOT_ARCH="amd64"
else
    echo "Could not determine the chroot's CPU architecture. Aborting." 1>&2
    exit 1
fi

# Ensure chroot has /proc and /dev/pts
mount -t proc proc "$CHROOT/proc"
mount -t devpts devpts "$CHROOT/dev/pts"

# Ensure chroot is up to date regarding versions
#chroot "$CHROOT" apt-get update
# Ensure the package cache is really empty.
chroot "$CHROOT" apt-get clean

# Some packages, notably MySQL Server, will ask for password during
# installation. Switch that off to allow automatic installation.
export DEBIAN_FRONTEND=noninteractive

if [ -n "$PACKAGES_NAMES" ]; then
    echo "installing these packages by name: $PACKAGES_NAMES"
    chroot "$CHROOT" apt-get -d --assume-yes install $PACKAGES_NAMES
else
    echo "no packages to install by name"
fi

if [ -n "$PACKAGES_FILES" ]; then
    echo "installing these package files: $PACKAGES_FILES"
    cp $PACKAGES_FILES "$CHROOT/tmp/"
    chroot "$CHROOT" bash -c 'dpkg -i /tmp/*.deb'
else
    echo "no packages to install by file"
fi

# Ensure that all unfulfilled dependencies are met.
chroot "$CHROOT" apt-get -f install


# We have no clue what kind of stuff was started in the chroot. Shut
# down everything that seems reasonable: All daemons started in runlevel 2.
( cd $CHROOT; for daemon in etc/rc2.d/S*; do chroot . $daemon stop; done )

# Unmount the chroot's has /proc and /dev/pts before we delete it
umount "$CHROOT/proc"
umount "$CHROOT/dev/pts"

# basic setup of repository
mkdir "$REPO_NAME"
mkdir "$REPO_NAME/conf"
echo "Origin: Axiros
Label: $REPO_NAME
Suite: stable
Codename: $CHROOT_VERSION
Version: $CHROOT_VERSION_NUMBER
Architectures: $CHROOT_ARCH source
Components: main non-free contrib
Description: Axiros Mobile Repository
SignWith: yes" > "$REPO_NAME/conf/distributions"

# There may not be any packages in the cache, in which case
# ..../archives/*.deb will not expand to anything and instead is
# interpreted literally.
for package in $PACKAGES_FILES $(find "$CHROOT/var/cache/apt/archives" -name '*.deb'); do
    echo "Adding file $package to repository"
    reprepro -Vb $REPO_NAME includedeb $CHROOT_VERSION $package
done

( cd "$REPO_NAME/.."; tar -czf "$REPO_NAME.tar.gz" `basename "$REPO_NAME"` )
echo "Tared repository is at $REPO_NAME.tar.gz"

exit 0

