#
# spec file for package libvorbis
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libvorbis
Version:        1.3.3
Release:        0
License:        BSD-3-Clause
#to_be_filled_by_service
Summary:        The Vorbis General Audio Compression Codec
Url:            http://www.vorbis.com/
Group:          System/Libraries
# bug437293 (SLES10 -> SLES11 upgrade path)
%ifarch ppc64
Obsoletes:      libvorbis-64bit
%endif
#
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Patch1:         libvorbis-lib64.dif
Patch2:         libvorbis-m4.dif
# URL http://www.geocities.jp/aoyoume/aotuv/
# 'Patch5:         libvorbis-%%{version}-aotuv-b5.7.diff'
# PATCH-FIX-UPSTREAM libvorbis-pkgconfig.patch https://trac.xiph.org/ticket/1759 reddwarf@opensuse.org -- Use Requires/Libs.private to avoid overlinking
Patch10:        libvorbis-pkgconfig.patch
Patch11:        vorbis-fix-linking.patch
Patch12:        vorbis-ocloexec.patch
BuildRequires:  fdupes
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbis0

Summary:        The Vorbis General Audio Compression Codec
Group:          System/Libraries
# bug437293 (SLES10 -> SLES11 upgrade path)
%ifarch ppc64
Obsoletes:      libvorbis-64bit
%endif
#
# libvorbis was last used in openSUSE 11.3
Provides:       %{name} = 1.3.2
Obsoletes:      %{name} < 1.3.2

%description -n libvorbis0
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbisenc2

Summary:        The Vorbis General Audio Compression Codec
Group:          System/Libraries

%description -n libvorbisenc2
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbisfile3

Summary:        The Vorbis General Audio Compression Codec
Group:          System/Libraries

%description -n libvorbisfile3
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package devel
Summary:        Include Files and Libraries mandatory for Ogg Vorbis Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libogg-devel
Requires:       libvorbis0 = %{version}
Requires:       libvorbisenc2 = %{version}
Requires:       libvorbisfile3 = %{version}
# bug437293 (SLES10 -> SLES11 upgrade path)
%ifarch ppc64
Obsoletes:      libvorbis-devel-64bit
%endif
#

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libvorbis.

%package doc
Summary:        Documentation of Ogg/Vorbis library
Group:          Documentation/Other
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
This package contains documents for Ogg/Vorbis library, including the
API reference.

%prep
%setup -q
%patch2
# %%patch5 -p1
%patch10
if [ "%{_lib}" == "lib64" ]; then
%patch1
fi
%patch11
%patch12

%build
# Fix optimization level
sed -i s,-O20,-O3,g configure.ac

autoreconf -fiv
%configure --disable-examples --disable-static
make %{?_smp_mflags}

%check
make check

%install
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/libvorbis-* %{buildroot}%{_docdir}/%{name}
install -c -m 0644 doc/Vorbis_I_spec.* %{buildroot}%{_docdir}/%{name}
# remove unneeded files
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot}%{_docdir}/ -empty -delete
%fdupes -s %{buildroot}%{_docdir}


%post -n libvorbis0 -p /sbin/ldconfig

%postun -n libvorbis0 -p /sbin/ldconfig

%post -n libvorbisenc2 -p /sbin/ldconfig

%postun -n libvorbisenc2 -p /sbin/ldconfig

%post -n libvorbisfile3 -p /sbin/ldconfig

%postun -n libvorbisfile3 -p /sbin/ldconfig

%files -n libvorbis0
%defattr(0644,root,root,0755)
%{_libdir}/libvorbis.so.0*

%files -n libvorbisenc2
%defattr(0644,root,root,0755)
%{_libdir}/libvorbisenc.so.2*

%files -n libvorbisfile3
%defattr(0644,root,root,0755)
%{_libdir}/libvorbisfile.so.3*

%files devel
%defattr(-,root,root)
%doc COPYING AUTHORS README *.txt
%{_datadir}/aclocal/*.m4
%{_includedir}/vorbis
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}

%changelog
