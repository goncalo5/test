#!/bin/bash
MAKE_CHROOT=${MAKE_CHROOT:-"./make_chroot.sh"}
[ -x "$MAKE_CHROOT" ] || {
    echo "make_chroot script not found at <$MAKE_CHROOT> or not executable" >&2
    exit 1
}

WORKDIR=`mktemp -d`
[ -z "$WORKDIR" ] && {
    echo "Could not create temporary directory" 1>&2
    exit 1
}

DEACTIVATE_CHROOT=${DEACTIVATE_CHROOT:-"./deactivate_chroot.sh"}
[ -x "$DEACTIVATE_CHROOT" ] || {
    echo "deactivate_chroot script not found at <$DEACTIVATE_CHROOT> or not executable" >&2
    exit 1
}

# Where the tarfile should be placed. If not given, tarfile is placed in the
# temporary directory where the chroot is located
ARCHIVE_DIR=${ARCHIVE_DIR:-$WORKDIR}
# Should the chroot be removed after creation? Set to "yes" to remove it.
REMOVE_CHROOT=${REMOVE_CHROOT:-"yes"}

RELEASES=${RELEASES:-"squeeze wheezy jessie stretch"}
ARCHITECTURES=${ARCHITECTURES:-"amd64"}

# Otherwise, "dpkg-reconfigure tzinfo" will start and ask for user input.
export AX_TIMEZONE="Europe/Berlin"

echo "Building chroots for these releases: $RELEASES"
echo "Chroots are built for these architectures: $ARCHITECTURES"
echo -e "\tWorking in temporary directory <$WORKDIR>"
echo -e "\tTar balls will be stored in <$ARCHIVE_DIR>"
if [ "$REMOVE_CHROOT" = "yes" ]; then
    echo -e "\tChroots will be deleted after tar balls are created"
else
    echo -e "\tChroots will NOT be deleted after tar balls are created"
fi

{
for release in $RELEASES; do 
    for architecture in $ARCHITECTURES; do
        chroot_name="${release}_${architecture}_chroot"
        chroot_dir="$WORKDIR/$chroot_name"

        mkdir "$chroot_dir"
        location="local"
        [ "$release" = "etch" ] && location="remote"
        [ "$release" = "lenny" ] && location="remote"
        [ "$architecture" = "i386" ] && location="remote"

        # This output is picked up by "xargs", see below.
        echo "$architecture" "$release" "$chroot_dir" "$location"
    done
done
} | xargs --max-lines=1 --max-procs=8 nice ionice -n 7 ./make_chroot.sh

for release in $RELEASES; do
    for architecture in $ARCHITECTURES; do
        chroot_name="${release}_${architecture}_chroot"
        chroot_dir="$WORKDIR/$chroot_name"

        ${DEACTIVATE_CHROOT} "$chroot_dir"

        # make_chroot.sh copies the base system's /etc/hosts. This is a bad
        # idea during bulk-creation of chroots.
        echo "127.0.0.1         localhost
::1             ip6-localhost ip6-loopback
fe00::0         ip6-localnet
ff00::0         ip6-mcastprefix
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters
ff02::3         ip6-allhosts" > "$chroot_dir/etc/hosts"

        # make_chroot.sh copies the base system's /etc/resolv.conf. This is a
        # bad idea during bulk-creation of chroots. Use a resolv.conf that
        # works in Axiros' local network
        echo "nameserver 10.0.0.5" > "$chroot_dir/etc/resolv.conf"

        if [ -n "$ARCHIVE_DIR" ]; then
            # "cd" to the directory so that the tar-file will not contain the
            # path, but only the content.
            ( cd "$chroot_dir"; tar --numeric-owner -cf "$ARCHIVE_DIR/${chroot_name}.tar" ./ ; )
        else
            ( cd "$chroot_dir"; tar --numeric-owner -cf "${chroot_name}.tar" ./ ; )
        fi

        [ "x$REMOVE_CHROOT" = xyes ] && rm -r "$chroot_dir"
    done
done

