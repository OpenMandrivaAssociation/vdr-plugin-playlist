
%define plugin	playlist
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define prever	rc3
%define rel	9
%define release	0.%prever.%rel

Summary:	VDR plugin: playlist for recordings
Name:		%name
Version:	%version
Release:	%mkrel %release
Group:		Video
License:	GPL
URL:		http://www.fast-info.de/vdr/playlist/
Source:		http://www.fast-info.de/vdr/playlist/vdr-%plugin-%version%prever.tar.bz2
Patch0:		91_playlist-0.0.2-compile-fix.dpatch
Patch1:		92_playlist-0.0.2-buffer.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This is a plugin for VDR to allow having recording playlists.

%prep
%setup -q -n %plugin-%version
%patch0 -p1 -b .fix
%patch1 -p1 -b .buffer

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
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


