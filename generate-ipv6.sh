#!/usr/bin/env bash

#running this script will regenerate the ipv6 versions of the blocklist based on the contents of the IPv4 blocklist in the .txt files

SED=sed
unamestr=`uname`
if [[ "$unamestr" == "Darwin" ]] ; then
    SED=gsed
    type $SED >/dev/null 2>&1 || {
        echo >&2 "$SED it's not installed. Try: brew install gnu-sed" ;
        exit 1;
    }
fi

cp dnsmasq_hosts.txt dnsmasq_hosts.txt.ipv6
$SED -i 's/0.0.0.0 /::1 /g' dnsmasq_hosts.txt.ipv6

cp etc_hosts.txt etc_hosts.txt.ipv6
$SED -i 's/0.0.0.0 /::1 /g' etc_hosts.txt.ipv6

