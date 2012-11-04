Name:           libvorbis
Version:        1.3.3
Release:        0
License:        BSD-3-Clause
Summary:        The Vorbis General Audio Compression Codec
Url:            http://www.vorbis.com/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Patch1:         libvorbis-lib64.dif
Patch2:         libvorbis-m4.dif
Patch10:        libvorbis-pkgconfig.patch
Patch11:        vorbis-fix-linking.patch
Patch12:        vorbis-ocloexec.patch
BuildRequires:  fdupes
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.


%package -n libvorbisenc

Summary:        The Vorbis General Audio Compression Codec
Group:          System/Libraries

%description -n libvorbisenc
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbisfile

Summary:        The Vorbis General Audio Compression Codec
Group:          System/Libraries

%description -n libvorbisfile
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
Requires:       libvorbis = %{version}
Requires:       libvorbisenc = %{version}
Requires:       libvorbisfile = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libvorbis.

%package doc
Summary:        Documentation of Ogg/Vorbis library
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package contains documents for Ogg/Vorbis library, including the
API reference.

%prep
%setup -q

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
find %{buildroot}%{_docdir}/ -empty -delete
%fdupes -s %{buildroot}%{_docdir}


%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libvorbisenc -p /sbin/ldconfig

%postun -n libvorbisenc -p /sbin/ldconfig

%post -n libvorbisfile -p /sbin/ldconfig

%postun -n libvorbisfile -p /sbin/ldconfig

%files 
%defattr(0644,root,root,0755)
%{_libdir}/libvorbis.so.0*

%files -n libvorbisenc
%defattr(0644,root,root,0755)
%{_libdir}/libvorbisenc.so.2*

%files -n libvorbisfile
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
