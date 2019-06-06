Name:           nextspace-applications
Version:        0.85
Release:        1%{?dist}
Summary:        NextSpace desktop core applications.

Group:          Libraries/NextSpace
License:        GPLv2
URL:		http://www.github.com/trunkmaster/nextspace
Source0:	nextspace-applications-%{version}.tar.gz

Provides:	libWMUtil.so
Provides:	libWINGs.so

BuildRequires:	nextspace-frameworks-devel
# Preferences
#BuildRequires:	
# Login
BuildRequires:	pam-devel
# Workspace
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXft-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXmu-devel
BuildRequires:	libexif-devel
BuildRequires:	libXfixes-devel
BuildRequires:	fontconfig-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
#
Requires:	nextspace-frameworks
Requires:	fontconfig
Requires:	libXft
Requires:	libXinerama
Requires:	libXpm
Requires:	libXmu
Requires:	libXfixes
Requires:	libexif
Requires:	xorg-x11-drv-evdev
Requires:	xorg-x11-drv-intel
Requires:	xorg-x11-drv-vesa
Requires:	xorg-x11-drv-synaptics
Requires:	xorg-x11-drv-keyboard
Requires:	xorg-x11-drv-mouse
Requires:	xorg-x11-server-Xorg
Requires:	xorg-x11-server-utils
Requires:	xorg-x11-xkb-utils
Requires:	xorg-x11-fonts-100dpi
Requires:	xorg-x11-fonts-misc
Requires:	mesa-dri-drivers


%description
NextSpace desktop core applications.

%package devel
Summary:	NextSpace desktop core applications headers (Preferences, Workspace).
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header file for NextSpace core applications (Preferences, Workspace).

%prep
%setup

#
# Build phase
#
%build
export GNUSTEP_MAKEFILES=/Developer/Makefiles
make

#
# Build install phase
#
%install
export GNUSTEP_MAKEFILES=/Developer/Makefiles
export QA_SKIP_BUILD_ROOT=1
%{make_install}

#
# Files
#
%files
/Applications
/Library
/usr/NextSpace

%files devel
/usr/NextSpace/include

#
# Package install
#
#%pre

%post
systemctl enable /usr/NextSpace/Apps/Login.app/Resources/loginwindow.service
systemctl set-default graphical.target

%preun
systemctl disable loginwindow.service
systemctl set-default multi-user.target

#%postun

%changelog
* Fri May 24 2019 Sergii Stoian <stoyan255@gmail.com>  - 0.85-1
- Fixed more .gorm files due to framewrks refactoring.
- set default `graphical.target` to systemd.
* Sat May  4 2019 Sergii Stoian <stoyan255@gmail.com> - 0.85-0
- Prepare for 0.85 release.
* Fri Oct 21 2016 Sergii Stoian <stoyan255@gmail.com> 0.4-0
- Initial spec for CentOS 7.
