%define debug_package %{nil}

Name:		alertmanager
Version:	0.4.2
Release:	1%{?dist}
Summary:	The Alertmanager handles alerts sent by client applications such as the Prometheus server.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/alertmanager
Source0:	https://github.com/prometheus/alertmanager/releases/download/%{version}/alertmanager-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
AutoReqProv:	No

%description

The Alertmanager handles alerts sent by client applications such as the Prometheus server. 
It takes care of deduplicating, grouping, and routing them to the correct receiver integration such as email, PagerDuty, or OpsGenie. 
It also takes care of silencing and inhibition of alerts.

%prep
%setup -q -n %{name}-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/var/run/alertmanager
mkdir -vp $RPM_BUILD_ROOT/var/lib/alertmanager
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -vp $RPM_BUILD_ROOT/etc/alertmanager
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus/alertmanager

install -m 755 contrib/alertmanager.env $RPM_BUILD_ROOT/etc/alertmanager/alertmanager.env
install -m 755 contrib/alertmanager.service $RPM_BUILD_ROOT/usr/lib/systemd/system/alertmanager.service
install -m 644 contrib/alertmanager.yaml $RPM_BUILD_ROOT/etc/alertmanager/alertmanager.yaml
install -m 755 alertmanager $RPM_BUILD_ROOT/usr/bin/alertmanager

%clean

%pre
getent group alertmanager >/dev/null || groupadd -r alertmanager
getent passwd alertmanager >/dev/null || \
  useradd -r -g alertmanager -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/alertmanager/ -c "alertmanager Daemons" alertmanager
exit 0

%post
chgrp alertmanager /var/run/alertmanager
chmod 774 /var/run/alertmanager
chown alertmanager:alertmanager /var/lib/prometheus/alertmanager

%files
%defattr(-,root,root,-)
/usr/bin/alertmanager
%config(noreplace) /etc/alertmanager/alertmanager.yaml
%config(noreplace) /etc/alertmanager/alertmanager.env
/usr/lib/systemd/system/alertmanager.service
/var/lib/prometheus/alertmanager
/var/run/alertmanager
