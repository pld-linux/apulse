Summary:	PulseAudio emulation for ALSA
Summary(pl.UTF-8):	Emulacja PulseAudio dla Alsy
Name:		apulse
Version:	0.1.13
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/i-rinat/apulse/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	90a9608a1b30f221925fb363dc2580a6
URL:		https://github.com/i-rinat/apulse
BuildRequires:	alsa-lib-devel
BuildRequires:	glib2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program provides an alternative partial implementation of the
PulseAudio API. It consists of a loader script and a number of shared
libraries with the same names as from original PulseAudio, so
applications could dynamically load them and think they are talking to
PulseAudio. Internally, no separate sound mixing daemon is used.
Instead, apulse relies on ALSA's `dmix`, `dsnoop`, and `plug` plugins
to handle multiple sound sources and capture streams running at the
same time. `dmix` plugin muxes multiple playback streams; `dsnoop`
plugin allow multiple applications to capture from a single
microphone; and `plug` plugin transparently converts audio between
various sample formats, sample rates and channel numbers. For more
than a decade now, ALSA comes with these plugins enabled and
configured by default.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/apulse
%{_prefix}/lib/apulse/libpulse-mainloop-glib.so
%{_prefix}/lib/apulse/libpulse-mainloop-glib.so.0
%{_prefix}/lib/apulse/libpulse-simple.so
%{_prefix}/lib/apulse/libpulse-simple.so.0
%{_prefix}/lib/apulse/libpulse.so
%{_prefix}/lib/apulse/libpulse.so.0
%{_mandir}/man1/apulse.1*
