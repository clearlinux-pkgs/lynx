#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x702353E0F7E48EDB (dickey@invisible-island.net)
#
Name     : lynx
Version  : 1
Release  : 4
URL      : https://invisible-mirror.net/archives/lynx/tarballs/lynx2.8.9rel.1.tar.gz
Source0  : https://invisible-mirror.net/archives/lynx/tarballs/lynx2.8.9rel.1.tar.gz
Source1 : https://invisible-mirror.net/archives/lynx/tarballs/lynx2.8.9rel.1.tar.gz.asc
Summary  : A text-based Web browser
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: lynx-bin = %{version}-%{release}
Requires: lynx-data = %{version}-%{release}
Requires: lynx-license = %{version}-%{release}
Requires: lynx-locales = %{version}-%{release}
Requires: lynx-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : cppcheck
BuildRequires : ctags
BuildRequires : glibc-bin
BuildRequires : ncurses-dev
BuildRequires : openssl-dev
Patch1: 0001-Try-to-load-stateless-path-for-lynx-configs.patch

%description
Lynx is a fully-featured World Wide Web (WWW) client for users running
cursor-addressable, character-cell display devices.  It is very fast and easy
to use.  It will display HTML documents containing links to files residing on
the local system, as well as files residing on remote systems running Gopher,
HTTP, FTP, WAIS, and NNTP servers.

%package bin
Summary: bin components for the lynx package.
Group: Binaries
Requires: lynx-data = %{version}-%{release}
Requires: lynx-license = %{version}-%{release}

%description bin
bin components for the lynx package.


%package data
Summary: data components for the lynx package.
Group: Data

%description data
data components for the lynx package.


%package license
Summary: license components for the lynx package.
Group: Default

%description license
license components for the lynx package.


%package locales
Summary: locales components for the lynx package.
Group: Default

%description locales
locales components for the lynx package.


%package man
Summary: man components for the lynx package.
Group: Default

%description man
man components for the lynx package.


%prep
%setup -q -n lynx2.8.9rel.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568756778
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-ssl=/usr \
--enable-nls \
--enable-ipv6 \
--mandir=/usr/share/man \
--with-screen=ncurses
make  %{?_smp_mflags} LIBS="-lncursesw -lssl -lcrypto"

%install
export SOURCE_DATE_EPOCH=1568756778
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lynx
cp COPYING %{buildroot}/usr/share/package-licenses/lynx/COPYING
cp WWW/Library/vms/COPYING.LIB %{buildroot}/usr/share/package-licenses/lynx/WWW_Library_vms_COPYING.LIB
%make_install
%find_lang lynx
## install_append content
install -m 0755 -d %{buildroot}/usr/share/defaults/lynx/
install -m 0644 lynx.cfg %{buildroot}/usr/share/defaults/lynx/lynx.cfg
install -m 0644 samples/lynx.lss %{buildroot}/usr/share/defaults/lynx/lynx.lss
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lynx

%files data
%defattr(-,root,root,-)
/usr/share/defaults/lynx/lynx.cfg
/usr/share/defaults/lynx/lynx.lss

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lynx/COPYING
/usr/share/package-licenses/lynx/WWW_Library_vms_COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lynx.1

%files locales -f lynx.lang
%defattr(-,root,root,-)

