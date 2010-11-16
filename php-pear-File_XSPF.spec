%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	File_XSPF
Summary:	%{_pearname} - manipulating XSPF playlists
Summary(pl.UTF-8):	%{_pearname} - manipulowanie playlistami XSPF
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d2956d070e7dd6b734a94478daa6c318
URL:		http://pear.php.net/package/File_XSPF/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.a1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.0-0.a1
Requires:	php-pear-Validate >= 0.6.2
Requires:	php-pear-XML_Parser >= 1.2.7
Requires:	php-pear-XML_Tree >= 1.1.0
Obsoletes:	php-pear-File_XSPF-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the user with the ability to update and create
XSPF playlist files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza użytkownikowi możliwość tworzenia i aktualizacji
plików playlist w formacie XSPF.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/File/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/XSPF.php
%{php_pear_dir}/File/XSPF

%{_examplesdir}/%{name}-%{version}
