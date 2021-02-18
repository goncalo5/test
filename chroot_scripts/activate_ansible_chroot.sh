#!/bin/bash
# =============================================================================
# Ansible for AXTRACT - activate the control machine chroot
# =============================================================================
set -e

[ "$UID" != "0" ] && {
    echo "You need to be root to run this program" >&2
    exit 1
}
[ $# -lt 1 ] && {
    echo "Please provide the Ansible for AXTRACT chroot tarball filename" >&2
    exit 1
}

CHROOT_DIR=${DEPLOY_PATH:-"/opt/axtract-ansible"}
CHROOT_DIR=$(readlink -f $CHROOT_DIR)
AXTRACT_ANSIBLE_CHROOT_TARBALL=$(readlink -f $1)
SCRIPT_DIR=$(readlink -f $(dirname $0))

[ ! -f ${AXTRACT_ANSIBLE_CHROOT_TARBALL} ] && {
    echo "Ansible for AXTRACT chroot tarball <$AXTRACT_ANSIBLE_CHROOT_TARBALL> missing!" >&2
    exit 1
}
[ -d ${CHROOT_DIR} ] && {
    echo "chroot path <$CHROOT_DIR> already exists!" >&2
    exit 1
}

ACTIVATE_CHROOT=${ACTIVATE_CHROOT:-"${SCRIPT_DIR}/activate_chroot.sh"}
[ -x "$ACTIVATE_CHROOT" ] || {
    echo "activate_chroot script not found at <$ACTIVATE_CHROOT> or not executable" >&2
    exit 1
}
FINALIZE_CHROOT=${FINALIZE_CHROOT:-"${SCRIPT_DIR}/finalize_chroot.sh"}
[ -x "$FINALIZE_CHROOT" ] || {
    echo "finalize_chroot script not found at <$FINALIZE_CHROOT> or not executable" >&2
    exit 1
}

echo "Creating chroot directory ${CHROOT_DIR}" >&2
mkdir -p ${CHROOT_DIR}

echo "Extracting chroot tarball ${AXTRACT_ANSIBLE_CHROOT_TARBALL}" >&2
tar -xz -f ${AXTRACT_ANSIBLE_CHROOT_TARBALL} -C ${CHROOT_DIR}

echo "Activating chroot ${CHROOT_DIR}" >&2
${ACTIVATE_CHROOT} ${CHROOT_DIR}


if [ -f /etc/timezone ]; then
  export AX_TIMEZONE=`cat /etc/timezone`
elif [ -h /etc/localtime ]; then
  export AX_TIMEZONE=`readlink /etc/localtime | sed "s/\/usr\/share\/zoneinfo\///"`
else
  checksum=`md5sum /etc/localtime | cut -d' ' -f1`
  export AX_TIMEZONE=`find /usr/share/zoneinfo/ -type f -exec md5sum {} \; | grep "^$checksum" | sed "s/.*\/usr\/share\/zoneinfo\///" | head -n 1`
fi
echo "Finalizing chroot ${CHROOT_DIR}" >&2
${FINALIZE_CHROOT} ${CHROOT_DIR}

echo "Setting timezone" >&2
chroot ${CHROOT_DIR} dpkg-reconfigure -f noninteractive tzdata >/dev/null 2>&1

echo "Finished SUCESSFULLY" >&2
