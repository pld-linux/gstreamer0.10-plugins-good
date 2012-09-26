#
# Conditional build:
%bcond_without	aalib		# don't build aa videosink plugin
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	caca		# don't build caca videosink plugin
%bcond_without	cairo		# don't build cairo plugin
%bcond_with	esd		# build ESD plugin
%bcond_without	gconf		# don't build GConf plugin
%bcond_with	hal		# build HAL plugin
%bcond_without	jack		# don't build JACK audio plugin
%bcond_without	soup		# don't build libsoup 2.4 http source plugin
%bcond_without	speex		# don't build speex plugin
%bcond_without	wavpack		# don't build wavpack plugin

%define		gstname		gst-plugins-good
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.36
%define		gstpb_req_ver	0.10.36

%include	/usr/lib/rpm/macros.gstreamer
Summary:	Good GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Dobre wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer0.10-plugins-good
Version:	0.10.31
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-good/%{gstname}-%{version}.tar.xz
# Source0-md5:	555845ceab722e517040bab57f9ace95
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.8.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.24
BuildRequires:	gstreamer0.10-devel >= %{gst_req_ver}
BuildRequires:	gstreamer0.10-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	gtk+2-devel >= 2:2.14.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
BuildRequires:	libtool >= 1.4
BuildRequires:	orc-devel >= 0.4.11
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
##
## plugins
##
%{?with_gconf:BuildRequires:	GConf2-devel >= 2.14.0}
%{?with_aalib:BuildRequires:	aalib-devel >= 0.11.0}
BuildRequires:	bzip2-devel
%{?with_cairo:BuildRequires:	cairo-devel >= 1.2.0}
%{?with_cairo:BuildRequires:	cairo-gobject-devel >= 1.10.0}
BuildRequires:	dbus-devel >= 0.91
%{?with_esd:BuildRequires:	esound-devel >= 0.2.12}
BuildRequires:	flac-devel >= 1.1.4
%{?with_hal:BuildRequires:	hal-devel >= 0.5.7.1}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.99.10}
BuildRequires:	libavc1394-devel
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libdv-devel >= 0.104
BuildRequires:	libiec61883-devel >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libraw1394-devel >= 2.0.0
BuildRequires:	libshout-devel >= 2.0
%{?with_soup:BuildRequires:	libsoup-devel >= 2.26}
# for taglib
BuildRequires:	libstdc++-devel
BuildRequires:	libv4l-devel
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pulseaudio-devel >= 1.0
%{?with_speex:BuildRequires:	speex-devel >= 1:1.1.6}
BuildRequires:	taglib-devel >= 1.5
BuildRequires:	udev-glib-devel >= 143
%{?with_wavpack:BuildRequires:	wavpack-devel >= 4.40.0}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	zlib-devel
Requires:	glib2 >= 1:2.24
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	orc >= 0.4.11
Obsoletes:	gstreamer-avi
Obsoletes:	gstreamer-flx
%{!?with_hal:Obsoletes:	gstreamer-hal}
Obsoletes:	gstreamer-matroska
Obsoletes:	gstreamer-mixer
Obsoletes:	gstreamer-navigation
Obsoletes:	gstreamer-oss4
Obsoletes:	gstreamer-rtp
Obsoletes:	gstreamer-udp
%if %{without esd}
Obsoletes:	gstreamer-audiosink-esd
%endif
Conflicts:	gstreamer-plugins-bad < 0.10.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

%package apidocs
Summary:	Good GStreamer streaming-media framework plugins API documentation
Summary(pl.UTF-8):	Dokumentacja API dobrych wtyczek środowiska obróbki strumieni GStreamer
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Good GStreamer streaming-media framework plugins API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API dobrych wtyczek środowiska obróbki strumieni
GStreamer.

%package -n gstreamer0.10-GConf
Summary:	GStreamer GConf schemas
Summary(pl.UTF-8):	Schematy GConf GStreamera
Group:		Libraries
Requires(post,preun):	GConf2
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-GConf-devel

%description -n gstreamer0.10-GConf
Installation of GStreamer GConf schemas. These set usable defaults
used by all GStreamer-enabled GNOME applications.

%description -n gstreamer0.10-GConf -l pl.UTF-8
Schematy GConf dla GStreamera. Zestaw ten ustawia wartości domyślne
dla wszystkich aplikacji GNOME korzystających z GStreamera

## ## Plugins ##

%package -n gstreamer0.10-videosink-aa
Summary:	GStreamer plugin for Ascii-art output
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu Ascii-art do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Provides:	gstreamer0.10-videosink = %{version}
Obsoletes:	gstreamer-aalib

%description -n gstreamer0.10-videosink-aa
Plugin for viewing movies in Ascii-art using aalib library.

%description -n gstreamer0.10-videosink-aa -l pl.UTF-8
Wtyczka wyjścia obrazu Ascii-art używająca biblioteki aalib.

%package -n gstreamer0.10-audio-effects-good
Summary:	Good GStreamer audio effects plugins
Summary(pl.UTF-8):	Dobre wtyczki efektów dźwiękowych do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-audio-effects

%description -n gstreamer0.10-audio-effects-good
Good GStreamer audio effects plugins.

%description -n gstreamer0.10-audio-effects-good -l pl.UTF-8
Dobre wtyczki efektów dźwiękowych do GStreamera.

%package -n gstreamer0.10-audio-formats
Summary:	GStreamer audio format plugins
Summary(pl.UTF-8):	Wtyczki formatów dźwięku
Group:		Libraries
#Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
# for locales in wavparse module
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer0.10-audio-formats
Plugin for playback of WAV, au and mod audio files as well as MP3
type.

%description -n gstreamer0.10-audio-formats -l pl.UTF-8
Wtyczka do odwarzania dźwięku w formacie au, WAV, mod oraz MP3.

%package -n gstreamer0.10-cairo
Summary:	GStreamer cairo plugin
Summary(pl.UTF-8):	Wtyczka cairo do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}

%description -n gstreamer0.10-cairo
GStreamer cairo plugin.

%description -n gstreamer0.10-cairo -l pl.UTF-8
Wtyczka cairo do GStreamera.

%package -n gstreamer0.10-dv
Summary:	GStreamer dv plugin
Summary(pl.UTF-8):	Wtyczka dv do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer0.10-dv
Plugin for digital video support.

%description -n gstreamer0.10-dv -l pl.UTF-8
Wtyczka do GStreamera obsługująca cyfrowy obraz.

%package -n gstreamer0.10-audiosink-esd
Summary:	GStreamer plugin for ESD sound output
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku ESD do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer0.10-audiosink = %{version}
Obsoletes:	gstreamer-esound

%description -n gstreamer0.10-audiosink-esd
Output plugin for GStreamer for use with the esound package.

%description -n gstreamer0.10-audiosink-esd -l pl.UTF-8
Wtyczka wyjścia dźwięku ESD (esound) dla GStreamera.

%package -n gstreamer0.10-flac
Summary:	GStreamer plugin for FLAC lossless audio format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca bezstratny format dźwięku FLAC
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	flac >= 1.1.4

%description -n gstreamer0.10-flac
Plugin for the free FLAC lossless audio format.

%description -n gstreamer0.10-flac -l pl.UTF-8
Wtyczka obsługująca wolnodostępny, bezstratny format dźwięku FLAC.

%package -n gstreamer0.10-gdkpixbuf
Summary:	GStreamer images input plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera wczytująca obrazki
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}

%description -n gstreamer0.10-gdkpixbuf
This GStreamer plugin load images via gdkpixbuf library.

%description -n gstreamer0.10-gdkpixbuf -l pl.UTF-8
Ta wtyczka GStreamera wczytuje obrazki za pośrednictwem biblioteki
gdkpixbuf.

%package -n gstreamer0.10-hal
Summary:	GStreamer plugin to wrap the GStreamer/HAL audio input/output devices
Summary(pl.UTF-8):	Wtyczka GStreamera spinająca urządzenia wejścia/wyjścia dźwięku z HAL-em
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}

%description -n gstreamer0.10-hal
GStreamer plugin to wrap the GStreamer/HAL audio input/output devices.

%description -n gstreamer0.10-hal -l pl.UTF-8
Wtyczka GStreamera spinająca urządzenia wejścia/wyjścia dźwięku między
GStreamerem a HAL-em.

%package -n gstreamer0.10-jack
Summary:	GStreamer plugin for the JACK Sound Server
Summary(pl.UTF-8):	Wtyczka serwera dźwięku JACK dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer0.10-audiosink = %{version}

%description -n gstreamer0.10-jack
Plugin for the JACK professional sound server.

%description -n gstreamer0.10-jack -l pl.UTF-8
Wtyczka dla profesjonalnego serwera dźwięku JACK.

%package -n gstreamer0.10-videosink-libcaca
Summary:	GStreamer plugin for libcaca Ascii-art output
Summary(pl.UTF-8):	Wtyczka libcaca do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer0.10-videosink = %{version}

%description -n gstreamer0.10-videosink-libcaca
GStreamer plug-in for libcaca Ascii-art output.

%description -n gstreamer0.10-videosink-libcaca -l pl.UTF-8
Wtyczka libcaca do GStreamera.

%package -n gstreamer0.10-libpng
Summary:	GStreamer plugin to encode png images
Summary(pl.UTF-8):	Wtyczka GStreamera kodująca pliki png
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	libpng >= 1.2.0

%description -n gstreamer0.10-libpng
Plugin for encoding png images.

%description -n gstreamer0.10-libpng -l pl.UTF-8
Wtyczka kodująca pliki png.

%package -n gstreamer0.10-audiosink-oss
Summary:	GStreamer plugins for input and output using OSS
Summary(pl.UTF-8):	Wtyczki wejścia i wyjścia dźwięku OSS do GStreamera
Group:		Libraries
#Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer0.10-audiosink = %{version}
Obsoletes:	gstreamer-oss

%description -n gstreamer0.10-audiosink-oss
Plugins for output and input to the OpenSoundSystem audio drivers
found in the Linux kernels or commercially available from OpenSound.

%description -n gstreamer0.10-audiosink-oss -l pl.UTF-8
Wtyczki wyjścia i wejścia dźwięku używające sterowników
OpenSoundSystem obecnych w jądrach Linuksa lub dostępnych komercyjnie
od OpenSound.

%package -n gstreamer0.10-pulseaudio
Summary:	GStreamer plugin for PulseAudio sound server
Summary(pl.UTF-8):	Wtyczka GStreamera dla serwera dźwięku PulseAudio
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	pulseaudio >= 1.0
Obsoletes:	gstreamer-audiosink-polypaudio
Provides:	gstreamer0.10-audiosink = %{version}
Obsoletes:	gstreamer-polypaudio

%description -n gstreamer0.10-pulseaudio
GStreamer plugin for PulseAudio sound server.

%description -n gstreamer0.10-pulseaudio -l pl.UTF-8
Wtyczka GStreamera dla serwera dźwięku PulseAudio.

%package -n gstreamer0.10-raw1394
Summary:	GStreamer raw1394 Firewire plugin
Summary(pl.UTF-8):	Wtyczka FireWire dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}

%description -n gstreamer0.10-raw1394
Plugin for digital video support using raw1394.

%description -n gstreamer0.10-raw1394 -l pl.UTF-8
Wtyczka dająca dostęp do cyfrowego obrazu przy użyciu raw1394.

%package -n gstreamer0.10-shout2
Summary:	GStreamer plugin for communicating with Shoutcast servers
Summary(pl.UTF-8):	Wtyczka do GStreamera umożliwiająca komunikację z serwerami Shoutcast
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}

%description -n gstreamer0.10-shout2
GStreamer plugin for communicating with Shoutcast servers.

%description -n gstreamer0.10-shout2 -l pl.UTF-8
Wtyczka do GStreamera umożliwiająca komunikację z serwerami Shoutcast.

%package -n gstreamer0.10-soup
Summary:	GStreamer Soup plugin
Summary(pl.UTF-8):	Wtyczka biblioteki Soup dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gst_req_ver}
Requires:	libsoup >= 2.26

%description -n gstreamer0.10-soup
GStreamer Plugin for downloading files with Soup library.

%description -n gstreamer0.10-soup -l pl.UTF-8
Wtyczka GStreamera umożliwiająca ściąganie plików za pomocą biblioteki
Soup.

%package -n gstreamer0.10-speex
Summary:	GStreamer speex codec decoder/encoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca kodek Speex
Group:		Libraries
#Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	speex >= 1:1.1.6

%description -n gstreamer0.10-speex
GStreamer speex codec decoder/encoder plugin.

%description -n gstreamer0.10-speex -l pl.UTF-8
Wtyczka do GStreamera obsługująca kodek Speex.

%package -n gstreamer0.10-taglib
Summary:	GStreamer tag writing plugin based on taglib
Summary(pl.UTF-8):	Wtyczka GStreamera zapisująca znaczniki oparta na bibliotece taglib
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	taglib >= 1.5

%description -n gstreamer0.10-taglib
GStreamer tag writing plugin based on taglib.

%description -n gstreamer0.10-taglib -l pl.UTF-8
Wtyczka GStreamera zapisująca znaczniki oparta na bibliotece taglib.

%package -n gstreamer0.10-v4l2
Summary:	GStreamer Video4Linux2 input plugin
Summary(pl.UTF-8):	Wtyczka wejścia Video4Linux2 dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-glib >= 143

%description -n gstreamer0.10-v4l2
GStreamer plugin for accessing Video4Linux2 devices.

%description -n gstreamer0.10-v4l2 -l pl.UTF-8
Wtyczka GStreamera pozwalająca na dostęp do urządzeń Video4Linux2.

%package -n gstreamer0.10-video-effects
Summary:	GStreamer video effects plugins
Summary(pl.UTF-8):	Wtyczki efektów wideo do GStreamera
Group:		Libraries
# for locales in jpeg module
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer0.10-video-effects
GStreamer video effects plugins.

%description -n gstreamer0.10-video-effects -l pl.UTF-8
Wtyczki efektów wideo do GStreamera.

%package -n gstreamer0.10-visualisation
Summary:	GStreamer visualisations plugins
Summary(pl.UTF-8):	Wtyczki wizualizacji do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}

%description -n gstreamer0.10-visualisation
Various plugins for visual effects to use with audio. Included are
monoscope, spectrum, goom (2k4) and goom2k1.

%description -n gstreamer0.10-visualisation -l pl.UTF-8
Różne wtyczki efektów wizualnych do używania z dźwiękiem. Załączone:
monoscope, spectrum, goom (2k4) i goom2k1.

%package -n gstreamer0.10-ximagesrc
Summary:	GStreamer X11 video input plugin using standard Xlib calls
Summary(pl.UTF-8):	Wtyczka wejścia obrazu X11 GStreamera używająca standardowych wywołań Xlib
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer0.10-ximagesrc
GStreamer X11 video input plugin using standard Xlib calls.

%description -n gstreamer0.10-ximagesrc -l pl.UTF-8
Wtyczka wejścia obrazu X11 GStreamera używająca standardowych wywołań
Xlib.

%package -n gstreamer0.10-wavpack
Summary:	GStreamer plugin for Wavpack lossless audio format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca bezstratny format dźwięku Wavpack
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	wavpack-libs >= 4.40.0

%description -n gstreamer0.10-wavpack
Plugin for lossless Wavpack audio format.

%description -n gstreamer0.10-wavpack -l pl.UTF-8
Wtyczka obsługująca bezstratny format dźwięku Wavpack.

%prep
%setup -q -n %{gstname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_lib_jpeg_mmx_jpeg_set_defaults=no \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	%{!?with_aalib:--disable-aalib} \
	%{!?with_cairo:--disable-cairo} \
	%{!?with_esd:--disable-esd} \
	%{!?with_jack:--disable-jack} \
	%{!?with_caca:--disable-libcaca} \
	%{!?with_soup:--disable-soup} \
	%{!?with_speex:--disable-speex} \
	%{!?with_wavpack:--disable-wavpack} \
	%{!?with_hal:--disable-hal} \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--enable-orc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n gstreamer0.10-GConf
%gconf_schema_install gstreamer-0.10.schemas

%preun	-n gstreamer0.10-GConf
%gconf_schema_uninstall gstreamer-0.10.schemas

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstalphacolor.so
%attr(755,root,root) %{gstlibdir}/libgstalpha.so
%attr(755,root,root) %{gstlibdir}/libgstannodex.so
%attr(755,root,root) %{gstlibdir}/libgstapetag.so
%attr(755,root,root) %{gstlibdir}/libgstaudiofx.so
%attr(755,root,root) %{gstlibdir}/libgstautodetect.so
%attr(755,root,root) %{gstlibdir}/libgstavi.so
%attr(755,root,root) %{gstlibdir}/libgstdebug.so
%attr(755,root,root) %{gstlibdir}/libgstefence.so
%attr(755,root,root) %{gstlibdir}/libgstequalizer.so
%attr(755,root,root) %{gstlibdir}/libgstdeinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstflv.so
%attr(755,root,root) %{gstlibdir}/libgstflxdec.so
%attr(755,root,root) %{gstlibdir}/libgsticydemux.so
%attr(755,root,root) %{gstlibdir}/libgstid3demux.so
%attr(755,root,root) %{gstlibdir}/libgstimagefreeze.so
%attr(755,root,root) %{gstlibdir}/libgstinterleave.so
%attr(755,root,root) %{gstlibdir}/libgstisomp4.so
%attr(755,root,root) %{gstlibdir}/libgstmatroska.so
%attr(755,root,root) %{gstlibdir}/libgstmultifile.so
%attr(755,root,root) %{gstlibdir}/libgstmultipart.so
%attr(755,root,root) %{gstlibdir}/libgstnavigationtest.so
%attr(755,root,root) %{gstlibdir}/libgstoss4audio.so
%attr(755,root,root) %{gstlibdir}/libgstreplaygain.so
%attr(755,root,root) %{gstlibdir}/libgstrtp.so
%attr(755,root,root) %{gstlibdir}/libgstrtpmanager.so
%attr(755,root,root) %{gstlibdir}/libgstrtsp.so
%attr(755,root,root) %{gstlibdir}/libgstshapewipe.so
%attr(755,root,root) %{gstlibdir}/libgstudp.so
%attr(755,root,root) %{gstlibdir}/libgstvideobox.so
%attr(755,root,root) %{gstlibdir}/libgstvideocrop.so
%attr(755,root,root) %{gstlibdir}/libgstvideofilter.so
%attr(755,root,root) %{gstlibdir}/libgstvideomixer.so
%attr(755,root,root) %{gstlibdir}/libgsty4menc.so
%dir %{_datadir}/gstreamer-0.10
%{_datadir}/gstreamer-0.10/presets

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-good-plugins-*
%endif

%if %{with gconf}
%files -n gstreamer0.10-GConf
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgconfelements.so
%{_sysconfdir}/gconf/schemas/gstreamer-0.10.schemas
%endif

##
## Plugins
##

%if %{with aalib}
%files -n gstreamer0.10-videosink-aa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstaasink.so
%endif

%files -n gstreamer0.10-audio-effects-good
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstalaw.so
%attr(755,root,root) %{gstlibdir}/libgstcutter.so
%attr(755,root,root) %{gstlibdir}/libgstlevel.so
%attr(755,root,root) %{gstlibdir}/libgstmulaw.so

%files -n gstreamer0.10-audio-formats
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstauparse.so
%attr(755,root,root) %{gstlibdir}/libgstaudioparsers.so
%attr(755,root,root) %{gstlibdir}/libgstwavparse.so
%attr(755,root,root) %{gstlibdir}/libgstwavenc.so

%if %{with cairo}
%files -n gstreamer0.10-cairo
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcairo.so
%endif

%files -n gstreamer0.10-dv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdv.so

%if %{with esd}
%files -n gstreamer0.10-audiosink-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstesd.so
%endif

%files -n gstreamer0.10-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstflac.so

%files -n gstreamer0.10-gdkpixbuf
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgdkpixbuf.so

%if %{with jack}
%files -n gstreamer0.10-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstjack.so
%endif

%if %{with hal}
%files -n gstreamer0.10-hal
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsthalelements.so
%endif

%if %{with caca}
%files -n gstreamer0.10-videosink-libcaca
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcacasink.so
%endif

%files -n gstreamer0.10-libpng
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstpng.so

%files -n gstreamer0.10-audiosink-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstossaudio.so

%files -n gstreamer0.10-pulseaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstpulse.so

%files -n gstreamer0.10-raw1394
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgst1394.so

%files -n gstreamer0.10-shout2
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstshout2.so

%if %{with soup}
%files -n gstreamer0.10-soup
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsouphttpsrc.so
%endif

%if %{with speex}
%files -n gstreamer0.10-speex
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspeex.so
%endif

%files -n gstreamer0.10-taglib
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttaglib.so

%files -n gstreamer0.10-v4l2
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux2.so

%files -n gstreamer0.10-video-effects
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsteffectv.so
%attr(755,root,root) %{gstlibdir}/libgstjpeg.so
%attr(755,root,root) %{gstlibdir}/libgstsmpte.so

%files -n gstreamer0.10-visualisation
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgoom.so
%attr(755,root,root) %{gstlibdir}/libgstgoom2k1.so
%attr(755,root,root) %{gstlibdir}/libgstmonoscope.so
%attr(755,root,root) %{gstlibdir}/libgstspectrum.so

%if %{with wavpack}
%files -n gstreamer0.10-wavpack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwavpack.so
%endif

%files -n gstreamer0.10-ximagesrc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstximagesrc.so
