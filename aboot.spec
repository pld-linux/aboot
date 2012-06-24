Summary:	A bootloader which can be started from the SRM console
Summary(pl):	Bootloader uruchamialny z konsoli SRM
Summary(pt_BR):	Bootloader para ser inicializado pelo firmware SRM
Name:		aboot
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://prdownloads.sourceforge.net/aboot/%{name}-%{version}.tar.gz
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
u�yciu SRM (zwykle u�ywanego do bootowania DEC UNIX). aboot pozwala na
tworzenie bootowalnych urz�dze� blokowych i zawiera program, kt�ry
mo�e bootowa� j�dra Linuksa z systemu plik�w bootowalnego dla SRM.
Obs�uguje tak�e bezpo�rednie bootowanie z wielu system�w plik�w (ext2,
ISO9660, UFS), bootowanie plik�w wykonywalnych (ELF i ECOFF),
bootowanie skompresowanych j�der, bootowanie z sieci (przez bootp),
tablice partycji w formacie DEC UNIX, interaktywne bootowanie oraz
standardowe konfiguracje konsol SRM, kt�re nie pozwalaj� na
przekazywanie d�ugich nazw opcji.

%description -l pt_BR
O programa aboot � a maneira recomendada para inicializar o Linux
quando � utilizado o firmware SRM (o firmware normalmente utilizado para
inicializar o DEC UNIX). Aboot suporta a cria��o de dispositivos
inicializ�veis e cont�m um programa que pode carregar o kernel Linux de
um sistema de arquivos que � inicializ�vel pelo SRM. Aboot tamb�m suporta
inicializa��o diretamente a partir de v�rios sistemas de arquivos (ext2,
ISO9660, UFS), carga de arquivos execut�veis (ELF e ECOFF), carga de kernels
compactados, boot remoto (utilizando bootp), tabelas de parti��o no formato
DEC UNIX, e inicializa��o interativa e configura��es default para consoles
SRM que n�o suportam a passagem de op��es longas.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} root=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) /sbin/*
%attr(640,root,root) /boot/bootlx
%{_mandir}/man8/*
%{_mandir}/man5/*
