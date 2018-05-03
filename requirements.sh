#!/bin/bash
# Find our package manager
if VERB="$( which apt-get )" 2> /dev/null; then
   echo "Installing libdbus-1-dev libdbus-glib-1-dev"
   sudo apt install -y libdbus-1-dev libdbus-glib-1-dev
elif VERB="$( which dnf )" 2> /dev/null; then
   echo "Installing dbus-devel dbus-glib-devel"
   sudo dnf install -y dbus-devel dbus-glib-devel
elif VERB="$( which zypper )" 2> /dev/null; then
   echo "Installing dbus-devel dbus-glib-devel"
   sudo zypper install -y dbus-devel dbus-glib-devel
else
   echo "Package Manager Not Found." >&2
   exit 1
fi
if [[ 1 -ne $# ]]; then
   exit 1
fi
$VERB "$1"
exit $?
