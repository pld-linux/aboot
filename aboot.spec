Summary: A bootloader which can be started from the SRM console.
Name: aboot
%define aboot_version 0.5
Version: %{aboot_version}
Release: 10
ExclusiveArch: alpha
Copyright: distributable
Group: System Environment/Base
Source: ftp://ftp.azstarnet.com/pub/linux/axp/aboot/aboot-%{aboot_version}.tar.gz
Patch0: aboot-0.5-make.patch.gz
Patch1: aboot-0.5-elf.patch.gz
Patch2: aboot-0.5-glibc2.patch.gz
Patch3: aboot-0.5-rth.patch.gz
Patch4: aboot-0.5-jay.patch
BuildRoot: /var/tmp/aboot-root

%description
The aboot program is the preferred way of booting Linux when using SRM
firmware (the firmware normally used to boot an DEC UNIX). Aboot supports
the creation of bootable block devices and contains a program which can
load Linux kernels from a filesystem which is bootable by SRM.  Aboot
also supports direct booting from various filesystems (ext2, ISO9660,
UFS), booting of executable object files (ELF and ECOFF), booting of
compressed kernels, network booting (using bootp), partition tables in
DEC UNIX format, and interactive booting and default configurations for
SRM consoles that cannot pass long option strings.

If you are installing Red Hat Linux on an Alpha, you'll need to install
the aboot package.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
chmod go= $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/man/man8
make root=$RPM_BUILD_ROOT install
cp -p sdisklabel/swriteboot.8 tools/e2writeboot.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc INSTALL README doc/*

%attr(644, root, root) /boot/bootlx
/sbin/abootconf
/sbin/e2writeboot
/sbin/isomarkboot
/sbin/swriteboot
/usr/man/man8/e2writeboot.8
/usr/man/man8/swriteboot.8
