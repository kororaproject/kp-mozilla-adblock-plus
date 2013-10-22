%global moz_extensions %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id \{d10d0bf8-f5b5-c8b4-a8b2-2b9879e08c5d\} 
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}

Name:           mozilla-adblock-plus
Version:        2.4
Release:        1%{?dist}
Summary:        Adblocking extension for Mozilla Firefox

Group:          Applications/Internet
License:        MPLv1.1
URL:            http://adblockplus.org
Source0:        https://adblockplus.org/downloads/adblockplus-%{version}.xpi
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       mozilla-adblockplus
Obsoletes:      mozilla-adblockplus
#Requires:       firefox

%description
Adblock Plus is a content-filtering extension for the Mozilla Firefox- and
Mozilla Application Suite-based web browsers. Adblock Plus allows users to
prevent page elements, such as advertisements, from being downloaded and
displayed.
It features improvements to the user interface, filter subscriptions, and
element hiding over the original Adblock extension.

%prep
%setup -q -c

%build
rm -rf %{buildroot}
install -Dp -m 644 bootstrap.js %{buildroot}%{inst_dir}/bootstrap.js
install -Dp -m 644 chrome.manifest %{buildroot}%{inst_dir}/chrome.manifest
install -Dp -m 644 icon64.png %{buildroot}%{inst_dir}/icon64.png
install -Dp -m 644 icon.png %{buildroot}%{inst_dir}/icon.png
install -Dp -m 644 install.rdf %{buildroot}%{inst_dir}/install.rdf
cp -a chrome %{buildroot}%{inst_dir}/
cp -a defaults %{buildroot}%{inst_dir}/
cp -a lib %{buildroot}%{inst_dir}/
cp -a META-INF %{buildroot}%{inst_dir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%doc license.txt
%{inst_dir}

%changelog
* Tue Oct 21 2013 Chris Smart <csmart@kororaproject.org>- 2.4-1
- Update to upstream 2.4 release

* Sun Aug 18 2013 Chris Smart <csmart@kororaproject.org>- 2.3.2-1
- Update to upstream 2.3.2 release

* Sat Mar 16 2013 Chris Smart <csmart@kororaproject.org>- 2.2.4-1
- Update to upstream 2.2.4 release

* Sat Mar 16 2013 Chris Smart <csmart@kororaproject.org>- 2.2.3-1
- Update to upstream 2.2.3 release

* Tue Jan 15 2013 Chris Smart <chris@kororaa.org>- 2.2.1-1
- Update to upstream 2.2.1 release

* Sat Sep 15 2012 Chris Smart <chris@kororaa.org>- 2.1.2-1
- Update to upstream 2.1.2 release

* Mon Jul 02 2012 Chris Smart <chris@kororaa.org>- 2.1-1
- Update to upstream 2.1 release

* Sat Feb 18 2012 Chris Smart <chris@kororaa.org>- 2.0.3-1
- Update to upstream 2.0.3 release

* Wed Jul 06 2011 Chris Smart <chris@kororaa.org>- 2.0.2-1
- Update to upstream 2.0.2 release

* Wed Jul 06 2011 Chris Smart <chris@kororaa.org>- 1.3.10-1
- Update to upstream 1.3.10 release
http://adblockplus.org/releases/adblock-plus-1310-released

* Wed Jul 06 2011 Chris Smart <chris@kororaa.org>- 1.3.9-1
- Update to upstream 1.3.9 release
http://adblockplus.org/releases/adblock-plus-139-released

* Sat May 28 2011 Chris Smart <chris@kororaa.org>- 1.3.8-1
- Update to upstream 1.3.8 release
http://adblockplus.org/releases/adblock-plus-138-released

* Fri Apr 08 2011 Chris Smart <chris@kororaa.org>- 1.3.6-1
- Update to upstream 1.3.6 release
http://adblockplus.org/releases/adblock-plus-136-released

* Mon Mar 28 2011 Chris Smart <chris@kororaa.org>- 1.3.5-1
- Initial port.
