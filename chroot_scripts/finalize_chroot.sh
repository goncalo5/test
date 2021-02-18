# This script "finalizes" a Debian chroot with some default configuration
set +e
LANG=C

[ -z "$1" ] && {
    echo "Usage: $0 <chroot directory>"
    echo "$0 called without first parameter. Aborting!"
    exit 1
}

target=$1

SCRIPT_DIR=$(dirname $0)

# Copy ax_repo script into chroot
cp ${SCRIPT_DIR}/ax_repo ${target}/usr/local/bin/
chmod 755 ${target}/usr/local/bin/ax_repo

# The SNMP daemon does not even start if /etc/mtab is not there.
touch ${target}/etc/mtab


cat >${target}/etc/bash.bashrc_firstpart <<-EOF
	# Some distributions, e.g. RHEL 7.0, use a file system layout where /bin and
	# /sbin are only symlinks to /usr/bin and /usr/sbin. These distributions do
	# not need to have /bin and /sbin in \$PATH. But Debian Squeeze and Wheezy
	# have many essential binaries (cat, grep, gzip) in those locations. Since
	# \$PATH is inherited from the outside, it must be adapted inside the chroot
	# if necessary. /etc/bash.bashrc is the first thing that bash runs, so the
	# fixing must be done at the top(!) of this script.
	which cat 2>/dev/null 1>&2 || {
	    # Seems /bin is not in the path.
	    PATH="\$PATH:/bin:/sbin"
	}
EOF
mv ${target}/etc/bash.bashrc ${target}/etc/bash.bashrc_secondpart
cat ${target}/etc/bash.bashrc_firstpart  ${target}/etc/bash.bashrc_secondpart > \
    ${target}/etc/bash.bashrc
rm -f ${target}/etc/bash.bashrc_firstpart  ${target}/etc/bash.bashrc_secondpart

# Allow big history for root and newly created users. Also tell programs
# (e.g. midnight commander) to use vim for editing via $EDITOR.
# LANG=C means no localization is used. This will speed up grep, sed, awk
# and friends greatly (5 times faster has been seen). Plus, it prevents
# lots of error messages if language settings outside the chroot do not
# match the inside.
cat >${target}/etc/profile.d/axiros_shell.sh <<-EOF
	PS1='\${debian_chroot:+\[\033[01;32m\]\$debian_chroot\[\033[00m\]} \u@\h:\w\\$ '
	export PS1="\[\e]0;\${debian_chroot:+(\$debian_chroot)}\u@\h:\w\a\]\$PS1"
	export HISTSIZE=50000
	export HISTTIMEFORMAT='%F %T '
	export EDITOR=vim
	export LANG=C
	unset LC_CTYPE
	unset LC_ALL
    unset LC_MESSAGES
	export HISTCONTROL=\$HISTCONTROL\${HISTCONTROL+:}ignoredups
EOF
chmod 755 ${target}/etc/profile.d/axiros_shell.sh

cp ${SCRIPT_DIR}/finalize_addons/z.sh ${target}/etc/profile.d
chmod 755 ${target}/etc/profile.d/z.sh

grep -qsF "# Axiros aliases" ${target}/etc/bash.bashrc || cat >> ${target}/etc/bash.bashrc <<- "EOF"
	# Axiros aliases+shortcuts
	alias ..="cd .."
	alias ...="cd ../.."
	alias l="ls -alF --color"
	# This defines a combined cd+ls command, use it like "cl /etc"
	cl() { [ -z "$1" ] && { echo "cl command needs a pathname"; } || { cd -- "$1" && l; } }

EOF

grep -qsF "shopt -q login_shell" ${target}/etc/bash.bashrc || cat >> ${target}/etc/bash.bashrc <<- "EOF"
	# We're typically not using a login shell inside a chroot but we
	# definitely want it to behave like one so lets import all those fancy
	# profiles when we're officially not a login shell
	shopt -q login_shell
	if [ $? -eq 1 ]; then
	    if [ -d /etc/profile.d ]; then
	      for i in /etc/profile.d/*.sh; do
	        if [ -r $i ]; then
	          . $i
	        fi
	      done
	      unset i
	    fi
	fi

EOF

# Add Axiros key to trusted keys
chroot ${target} <<EOF
# Trust Axiros repositories
# Key fingerprint: 4BB6 59B2 91AF 9495 4000  9DD4 A793 0025 9E90 FE23
echo "-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.10 (GNU/Linux)

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
FmJRtfzLXjgpUIwWCsew
=oSxg
-----END PGP PUBLIC KEY BLOCK-----" | apt-key add -
EOF

# Set up a vimrc (the EOF trick is called a "here document"). The last EOF must
# not be indented. Also note that the lines in the here-document need to remain
# indented by tabs.
mkdir -p ${target}/etc/vim
cat >${target}/etc/vim/vimrc.local <<- "EOF"
	iab Pdb import pdb; pdb.set_trace()
	syntax enable
	set encoding=utf8
	set tabstop=4
	set expandtab
	set softtabstop=4
	set backspace=indent,eol,start
	set shiftwidth=4
	set smarttab
	set number
	" in insert mode switch to paste mode AND back after paste using ctrl-u:
	set wildmode=list:full wildmode=longest,list pastetoggle=<c-u>
	" mouse scrolling plus select and copy via y or normal clipboard copy cmd:
	set clipboard^=unnamed
	set mouse-=a
	set incsearch
	set hlsearch
	map <S-F8> :nohlsearch<ENTER>
	set ignorecase
	set smartcase
	set autoindent
	set ruler
	filetype indent on
	filetype plugin on
	map <C-Down> ddp
	map <C-Up> kddpk
	set autoread
	set nodigraph
	set laststatus=2
	set novisualbell
	let python_highlight_all = 1
	let python_slow_sync=1
	command Pylint  !pylint -r no %
	command -nargs=* -complete=dir -complete=file Pyrun  !python % <args>
	autocmd FileType python set omnifunc=pythoncomplete#Complete
	inoremap <Nul> <C-x><C-o>
	set autowrite
	autocmd BufRead *.py set makeprg=python\ -c\ \"import\ py_compile,sys;\ sys.stderr=sys.stdout;\ py_compile.compile(r'%')\"
	augroup filetypedetect
	    au! BufNewFile,BufRead *.pt,*.cpt,*.ehf,*.zpt,*.rml   set tabstop=2 ft=xml shiftwidth=2
	augroup END
	"set background=dark
	"colorscheme axiros
	"colorscheme solarized
	"colorscheme BusyBee
	highlight OverLength ctermbg=green ctermfg=white guibg=#592929
	match OverLength /\%81v.\+/
EOF

# Without this setting, multitail may complain about "Could not determine size of file...."
echo -e '\n#Axiros make_chroot.sh setting:\ncheck_mail:0' >> ${target}/etc/multitail.conf

# Overwrite default inputrc with one that allows history search
cp ${SCRIPT_DIR}/finalize_addons/inputrc ${target}/etc/inputrc

# some vim colorschemes as a choice:
mkdir -p ${target}/usr/share/vim/vim72/colors
cp ${SCRIPT_DIR}/finalize_addons/*.vim ${target}/usr/share/vim/vim72/colors

chroot ${target} <<EOF
{
set +e
LANG=C

# Add all users we may possibly need from the very beginning. This way
# they have the same numeric user ID in all chroots.
# "--system" already indicates shell=/bin/false, --no-create-home and no
# asking for a password for this user.
adduser --uid 210 --group --system --home /opt/axess axess
adduser --uid 211 --group --system --home /opt/dhcpd dhcpd
adduser --uid 212 --group --system --home /opt/axtract axtract
adduser --uid 213 --group --system --home /var/lib/beanstalkd beanstalkd
adduser --uid 214 --group --system --home /home/mongodb mongodb
adduser --uid 215 --group --system --home /var/lib/mysql mysql
adduser --uid 216 --group --system --home /var/lib/snmp --shell /usr/sbin/nologin snmp
adduser --uid 217 --group --system --home /etc/freeradius freerad &&
    usermod --groups shadow freerad
# Without --force-badname, the user is not created
adduser --uid 218 --group --system --home /var/spool/exim4 --force-badname Debian-exim
}
EOF

# Select time zone. Either manually or take from environment variable.
if [ -n "$AX_TIMEZONE" ]; then
    echo "$AX_TIMEZONE" > ${target}/etc/timezone
    cp "/usr/share/zoneinfo/$AX_TIMEZONE" ${target}/etc/localtime
else
    chroot ${target} dpkg-reconfigure tzdata
fi

# Enable LS_OPTIONS for root in the chroot
sed -i "/# export LS_OPTIONS/c export LS_OPTIONS='-lha --color=auto --time-style=long-iso'" ${target}/root/.bashrc
sed -i "s/# alias ls/alias ls/" ${target}/root/.bashrc

# Add .ssh dir in root's dir
mkdir ${target}/root/.ssh

# Remove the cache of apt to make the chroot smaller
chroot ${target} apt-get clean

# Even now, ~28MB of cache data remain for Squeeze. After gzipping, they
# are still 11MB. The next "apt-get install ..." will rebuild these files
# within ~1 second, so might as well remove them.
rm -f ${target}/var/cache/apt/pkgcache.bin
rm -f ${target}/var/cache/apt/srcpkgcache.bin

# The "chroot ${target} <<EOF" commands are in the bash history -> clean up.
rm -f ${target}/root/.bash_history
