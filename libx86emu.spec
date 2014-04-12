Summary:	x86 CPU real mode emulator
Summary(pl.UTF-8):	Emulator trybu rzeczywistego procesorów Intel x86
Name:		libx86emu
Version:	1.4
Release:	1
License:	MIT
Group:		Libraries
# also https://gitorious.org/x86emu/libx86emu/archive/%{version}.tar.gz
Source0:	http://www.liwjatan.at/files/src/hwinfo/%{name}-%{version}.tar.xz
# Source0-md5:	4b46be2b22cf977defc1732d4472103f
URL:		https://gitorious.org/x86emu/libx86emu
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small x86 emulation library with focus of easy usage and extended
execution logging functions.

%description -l pl.UTF-8
Mała biblioteka emulacji x86, skupiająca się na łatwym użyciu i
rozszerzonych funkcjach do logowania wykonywania.

%package devel
Summary:	Header files for x86emu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki x86emu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	x86emu-devel < 1

%description devel
Header files for x86emu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki x86emu.

%package static
Summary:	Static x86emu library
Summary(pl.UTF-8):	Statyczna biblioteka x86emu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static x86emu library.

%description static -l pl.UTF-8
Statyczna biblioteka x86emu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -fomit-frame-pointer -Wall" \
	GIT2LOG=true \
	GITDEPS=

ar crs libx86emu.a *.o

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

install libx86emu.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libx86emu.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libx86emu.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx86emu.so
%{_includedir}/x86emu.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libx86emu.a
