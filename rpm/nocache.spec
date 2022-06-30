# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       nocache

# >> macros
# << macros

Summary:    minimize the effect on the file system cache
Version:    1.2
Release:    1
Group:      Applications/System
License:    BSD-2-Clause
URL:        https://github.com/Feh/nocache
Source0:    %{name}-%{version}.tar.gz
Source100:  nocache.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
The nocache tool tries to minimize the effect an application has on the Linux
file system cache. This is done by intercepting the open and close system calls
and calling posix_fadvise with the POSIX_FADV_DONTNEED parameter.
Because the library remembers which pages (ie., 4K-blocks of the file) were
already in file system cache when the file was opened, these will not be
marked as "don't need", because other applications might need that,
although they are not actively used (think: hot standby).

Use case: backup processes that should not interfere with the present state of the cache.

BUT: Read the README on github or under the Help link on why you probably
don't need this, and how to do what this tool does on a systemd system.

%if "%{?vendor}" == "chum"
PackageName: nocache
PackagerName: nephros
Type: console-application
Categories:
  - Utility
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/nocache
  Repo: https://github.com/Feh/nocache
Url:
  Help: https://github.com/Feh/nocache#if-you-use-systemd
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIR=%{_lib} all nocache.global
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
%__install -Dpm 0644 nocache.so %{buildroot}/%{_libdir}/nocache.so
%__install -Dpm 0755 nocache.global  %{buildroot}%{_bindir}/nocache
%__install -Dpm 0755 cachedel %{buildroot}%{_bindir}/cachedel
%__install -Dpm 0755 cachestats  %{buildroot}%{_bindir}/cachestats
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/nocache.so
%{_bindir}/*
# >> files
# << files
