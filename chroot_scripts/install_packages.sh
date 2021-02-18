#!/bin/bash
# This script installs packages to the changeroot
LANG=C

[ $# -lt 2 ] && {
    echo "Usage:"
    echo "$0 <chroot> <package1> [package2 [package3 ...]]"
    exit 1
}

target=$1
shift 1
packages=$*

POLICYFILE=$target/usr/sbin/policy-rc.d
POLICYFILE_ALREADY_EXISTS=no

if [ -f "${POLICYFILE}" ]; then
    POLICYFILE_ALREADY_EXISTS=yes
else
    # Create a policy file preventing init.d from scripts to be executed during
    # installation
    cat >>${POLICYFILE} <<EOF
#!/bin/sh
exit 101
EOF
    chmod +x ${POLICYFILE}
fi

DEBIAN_FRONTEND=noninteractive chroot $target apt-get update
DEBIAN_FRONTEND=noninteractive chroot $target apt-get upgrade --no-install-recommends --assume-yes --force-yes
DEBIAN_FRONTEND=noninteractive chroot $target apt-get install --no-install-recommends --assume-yes --force-yes $packages 
ret=$?
DEBIAN_FRONTEND=noninteractive chroot $target apt-get clean


if [ "x${POLICYFILE_ALREADY_EXISTS}" = "xno" ]; then
    rm -rf ${POLICYFILE}
fi

exit $ret
