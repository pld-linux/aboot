Summary:	A bootloader which can be started from the SRM console.
Name:		aboot
Version:	0.7a
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:        ftp://ftp.alphalinux.org/pub/Linux-Alpha/aboot/0.7a/%{name}-%{version}.tar.gz
Source1: 	http://www.itp.uni-hannover.de/~kreutzm/data/abootman.tar.bz2
#Patch0:		%{name}-0.5-make.patch.gz
#Patch1:		%{name}-0.5-elf.patch.gz
#Patch2:		%{name}-0.5-glibc2.patch.gz
#Patch3:		%{name}-0.5-rth.patch.gz
#Patch4:		%{name}-0.5-jay.patch
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

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8
install -d $RPM_BUILD_ROOT%{_mandir}/man5

%{__make} root=$RPM_BUILD_ROOT install

bzip2 -d -c %{SOURCE1} |tar x
cp *.8 $RPM_BUILD_ROOT%{_mandir}/man8
cp *.5 $RPM_BUILD_ROOT%{_mandir}/man5


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
