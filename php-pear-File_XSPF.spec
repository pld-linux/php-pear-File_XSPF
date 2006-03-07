%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	XSPF
%define		_status		beta
%define		_pearname	File_XSPF

Summary:	%{_pearname} - manipulating XSPF playlists
Summary(pl):	%{_pearname} - manipulowanie playlistami XSPF
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6b534045419ba79e4b15aa8fb73a7aae
URL:		http://pear.php.net/package/File_XSPF/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.0-0.a1
Requires:	php-pear-Validate >= 0.6.2
Requires:	php-pear-XML_Parser >= 1.2.7
Requires:	php-pear-XML_Tree >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the user with the ability to update and create
XSPF playlist files.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza u¿ytkownikowi mo¿liwo¶æ tworzenia i aktualizacji
plików playlist w formacie XSPF.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/XSPF.php
%{php_pear_dir}/File/XSPF
