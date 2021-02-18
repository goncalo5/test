#!/bin/bash

# Tool to compress many big tar files with gzip, bzip2 and lzma.

if [ -z $1 ]; then
    path="."
else
    path="$1"
fi

num_cores=`grep -c bogomips /proc/cpuinfo`
# /proc may not be mounted.
[ -z "$num_cores" -o "$num_cores" = "0" ] && num_cores=2

# LZMA processing, which is horribly CPU bound. With "xargs", multiple cores
# can be used. Do not wildly launch "lzma -7" processes, though, because they
# consume a lot of RAM.
if which lzma >/dev/null 2>/dev/null; then
    echo "compressing via lzma"
    # Sort by size: start big compression jobs first to minimize time until
    # all jobs are finished (=which is what we need to wait for).
    ( cd "$path"; ls -S1 *.tar | xargs --no-run-if-empty --max-args=1 --max-procs=$num_cores lzma -k -7 )
else
    echo "lzma not found, not compressing via lzma" >&2
fi

echo "compressing via gzip + bzip2"
which gzip >/dev/null 2>/dev/null && HAVE_GZIP=1 || HAVE_GZIP=0
if [ $HAVE_GZIP = 0 ]; then
    echo -e "\tgzip not found, not compressing via gzip" >&2
fi

if which pbzip2 >/dev/null 2>/dev/null; then
    HAVE_PBZIP2="1"
elif which bzip2 >/dev/null 2>/dev/null; then
    HAVE_BZIP2="1"
    HAVE_PBZIP2="0"
else
    echo "no bzip2/pbzip2 found, not compressing via (p)bzip2" >&2
    HAVE_BZIP2="0"
    HAVE_PBZIP2="0"
fi

# Launch all gzips in background...
[ $HAVE_GZIP = 1 ] && {
    echo compressing via gzip
    ( cd "$path"; ls -S1 *.tar  | xargs --no-run-if-empty --max-args=1 --max-procs=$num_cores -I file bash -c 'gzip -c file > file.gz' ; ) &
}

# ...then continue launching (p)bzip2 processes. At worst, we will have twice
# as many running threads as cores.
if [ $HAVE_PBZIP2 = 1 ]; then
    # Do not background or launch multiple processes. pbzip2 takes up all cpu cores, anyway.
    echo compressing via pbzip2
    ( cd "$path"; ls -S1 *.tar | xargs --no-run-if-empty --max-args=1 --max-procs=1 nice pbzip2 -k ) 
elif [ $HAVE_BZIP2 = 1 ]; then
    echo compressing via bzip2
    ( cd "$path"; ls -S1 *.tar | xargs --no-run-if-empty --max-args=1 --max-procs=$num_cores  bzip2 -k ) &
fi

# Ensure both gzipping and bzipping have finished.
wait
