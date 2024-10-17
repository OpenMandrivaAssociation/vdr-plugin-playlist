
%define plugin	playlist
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define prever	rc3
%define rel	17
%define release	0.%prever.%rel

Summary:	VDR plugin: playlist for recordings
Name:		%name
Version:	%version
Release:	%mkrel %release
Group:		Video
License:	GPL
URL:		https://www.linuxtv.org/vdrwiki/index.php/Playlist-plugin
Source:		http://www.fast-info.de/vdr/playlist/vdr-%plugin-%version%prever.tar.bz2
Patch0:		91_playlist-0.0.2rc3-fix-1.3.25.dpatch
Patch1:		93_playlist-0.0.2-1.5.7.dpatch
Patch2:		playlist-0.0.2-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a plugin for VDR to allow having recording playlists.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# show the plugin in the main menu
var=SHOW_MENU
param=-m
# hide the plugin from the main menu
var=HIDE_MENU
param=-M
# set name for the main menu entry
var=MENU_NAME
param="-n MENU_NAME"
# Show the delete all messages line at begin of messagelist
var=SHOW_DELETE_BEGIN
param=-b
# Hide the delete all messages line at begin of messagelist
var=HIDE_DELETE_BEGIN
param=-B
# Show the delete all messages line at end of messagelist
var=SHOW_DELETE_END
param=-e
# Hide the delete all messages line at end of messagelist
var=HIDE_DELETE_END
param=-E
# minimum entrys for display delete all messages
# line at begin and end (include -b and -e)
var=MIN_ENTRIES
param="-d MIN_ENTRIES"
# minimum time (min) for message in historyqueue (OSD-list) 5-999
var=HOLDTIME_HISTORY
param="-h HOLDTIME_HISTORY"
# minumum time (min) for responses in queue (readable by SAQRESP) 2-199
var=HOLDTIME_RESPONSES
param="-r HOLDTIME_RESPONSES"
# sortoption for messagelist (OSD)
var=SORT_ASCENDING
param=-s
# sortoption for messagelist (OSD)
var=SORT_DESCENDING
param=-S
# Enable more logging
var=VERBOSE
param=-v
# Disable more logging
var=NOVERBOSE
param=-V
# Hide the Prefer Command Line Parameter form setup-menu
var=HIDE_COMMANDLINE
param=--ns_commandline
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.15mdv2009.1
+ Revision: 359350
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.14mdv2009.0
+ Revision: 197962
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.13mdv2009.0
+ Revision: 197706
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- update URL
- adapt for api changes of VDR 1.3.25 (P0 from e-tobi)
- adapt for api changes of VDR 1.5.7 (P1 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.12mdv2008.1
+ Revision: 145174
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.11mdv2008.1
+ Revision: 103180
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.10mdv2008.0
+ Revision: 50030
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.9mdv2008.0
+ Revision: 42116
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.8mdv2008.0
+ Revision: 22768
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.7mdv2007.0
+ Revision: 90959
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.6mdv2007.1
+ Revision: 74069
- rebuild for new vdr
- Import vdr-plugin-playlist

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.2mdv2007.0
- rebuild for new vdr

* Tue Jul 18 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-0.rc3.1mdv2007.0
- initial Mandriva release

