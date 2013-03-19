Name:           libvorbis
Version:        1.3.3
Release:        0
License:        BSD-3-Clause
Summary:        The Vorbis General Audio Compression Codec
Url:            http://www.vorbis.com/
Group:          Multimedia/Audio
Source:         %{name}-%{version}.tar.xz
Source2:        baselibs.conf
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
Group:          Multimedia/Audio

%description -n libvorbisenc
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package -n libvorbisfile

Summary:        The Vorbis General Audio Compression Codec
Group:          Multimedia/Audio

%description -n libvorbisfile
Vorbis is a fully open, nonproprietary, patent-and-royalty-free, and
general-purpose compressed audio format for audio and music at fixed
and variable bit rates from 16 to 128 kbps/channel.

The native bitstream format of Vorbis is libogg (Ogg). Alternatively,
libmatroska (matroska) can also be used.

%package devel
Summary:        Include Files and Libraries mandatory for Ogg Vorbis Development
Group:          Development/Libraries
Requires:       glibc-devel
Requires:       libogg-devel
Requires:       libvorbis = %{version}
Requires:       libvorbisenc = %{version}
Requires:       libvorbisfile = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libvorbis.

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

%remove_docs

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libvorbisenc -p /sbin/ldconfig

%postun -n libvorbisenc -p /sbin/ldconfig

%post -n libvorbisfile -p /sbin/ldconfig

%postun -n libvorbisfile -p /sbin/ldconfig

%files 
%defattr(0644,root,root,0755)
%license COPYING 
%{_libdir}/libvorbis.so.0*

%files -n libvorbisenc
%defattr(0644,root,root,0755)
%license COPYING 
%{_libdir}/libvorbisenc.so.2*

%files -n libvorbisfile
%defattr(0644,root,root,0755)
%license COPYING 
%{_libdir}/libvorbisfile.so.3*

%files devel
%defattr(-,root,root)
%license COPYING 
%{_datadir}/aclocal/*.m4
%{_includedir}/vorbis
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
