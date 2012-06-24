Summary:	A bootloader which can be started from the SRM console
Summary(pl.UTF-8):   Bootloader uruchamialny z konsoli SRM
Summary(pt_BR.UTF-8):   Bootloader para ser inicializado pelo firmware SRM
Name:		aboot
Version:	0.9b
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://aboot.sourceforge.net/tarballs/%{name}-%{version}.tar.gz
# Source0-md5:	00c35c192d320bb005ad9bead7043d2c
Patch0:		%{name}-doc_Makefile.patch
URL:		http://aboot.sourceforge.net/
BuildRequires:	kernel24-headers
ExclusiveArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Program aboot jest preferowanym sposobem bootowania Linuksa przy
użyciu SRM (zwykle używanego do bootowania DEC UNIX). aboot pozwala na
tworzenie bootowalnych urządzeń blokowych i zawiera program, który
może bootować jądra Linuksa z systemu plików bootowalnego dla SRM.
Obsługuje także bezpośrednie bootowanie z wielu systemów plików (ext2,
ISO9660, UFS), bootowanie plików wykonywalnych (ELF i ECOFF),
bootowanie skompresowanych jąder, bootowanie z sieci (przez bootp),
tablice partycji w formacie DEC UNIX, interaktywne bootowanie oraz
standardowe konfiguracje konsol SRM, które nie pozwalają na
przekazywanie długich nazw opcji.

%description -l pt_BR.UTF-8
O programa aboot é a maneira recomendada para inicializar o Linux
quando é utilizado o firmware SRM (o firmware normalmente utilizado para
inicializar o DEC UNIX). Aboot suporta a criação de dispositivos
inicializáveis e contém um programa que pode carregar o kernel Linux de
um sistema de arquivos que é inicializável pelo SRM. Aboot também suporta
inicialização diretamente a partir de vários sistemas de arquivos (ext2,
ISO9660, UFS), carga de arquivos executáveis (ELF e ECOFF), carga de kernels
compactados, boot remoto (utilizando bootp), tabelas de partição no formato
DEC UNIX, e inicialização interativa e configurações default para consoles
SRM que não suportam a passagem de opções longas.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	KSRC=/usr/src/linux-2.4

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) /sbin/*
%attr(640,root,root) /boot/bootlx
%{_mandir}/man8/*
%{_mandir}/man5/*
