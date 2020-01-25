%define		status		beta
%define		pearname	File_XSPF
Summary:	%{pearname} - manipulating XSPF playlists
Summary(pl.UTF-8):	%{pearname} - manipulowanie playlistami XSPF
Name:		php-pear-%{pearname}
Version:	0.3.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	35a9a3b41d4ead8dbda36c83fcc3cca1
URL:		http://pear.php.net/package/File_XSPF/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.a1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten pakiet dostarcza użytkownikowi możliwość tworzenia i aktualizacji
plików playlist w formacie XSPF.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/File_XSPF/README .
mv docs/File_XSPF/examples .

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
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/XSPF.php
%{php_pear_dir}/File/XSPF
%{_examplesdir}/%{name}-%{version}
