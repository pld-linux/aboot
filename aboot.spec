Summary:	A bootloader which can be started from the SRM console
Summary(pl):	Bootloader uruchamialny z konsoli SRM
Name:		aboot
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(pl):	Aplikacje/System
Group(pt_BR):	Aplicações/Sistema
Source0:	ftp://ftp.alphalinux.org/pub/Linux-Alpha/aboot/0.9/%{name}-%{version}.tar.gz
Patch0:		%{name}-doc_Makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	alpha

%description
The aboot program is the preferred way of booting Linux when using SRM
firmware (the firmware normally used to boot an DEC UNIX). Aboot
supports the creation of bootable block devices and contains a program
which can load Linux kernels from a filesystem which is bootable by
SRM. Aboot also supports direct booting from various filesystems
(ext2, ISO9660, UFS), booting of executable object files (ELF and
ECOFF), booting of compressed kernels, network booting (using bootp),
partition tables in DEC UNIX format, and interactive booting and
default configurations for SRM consoles that cannot pass long option
strings.

%description -l pl
Program aboot jest preferowanym sposobem bootowania Linuksa przy
u¿yciu SRM (zwykle u¿ywanego do bootowania DEC UNIX). aboot pozwala na
tworzenie bootowalnych urz±dzeñ blokowych i zawiera program, który
mo¿e bootowaæ j±dra Linuksa z systemu plików bootowalnego dla SRM.
Obs³uguje tak¿e bezpo¶rednie bootowanie z wielu systemów plików (ext2,
ISO9660, UFS), bootowanie plików wykonywalnych (ELF i ECOFF),
bootowanie skompresowanych j±der, bootowanie z sieci (przez bootp),
tablice partycji w formacie DEC UNIX, interaktywne bootowanie oraz
standardowe konfiguracje konsol SRM, które nie pozwalaj± na
przekazywanie d³ugich nazw opcji.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} root=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz 
%attr(755,root,root) /sbin/*
%attr(640,root,root) /boot/bootlx
%{_mandir}/man8/*
%{_mandir}/man5/*
