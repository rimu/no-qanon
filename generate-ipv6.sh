#!/usr/bin/env bash
#running this script will regenerate the ipv6 versions of the blocklist based on the contents of the IPv4 blocklist in the .txt files

cp dnsmasq_hosts.txt dnsmasq_hosts.txt.ipv6
sed -i 's/0.0.0.0 /::1 /g' dnsmasq_hosts.txt.ipv6

cp etc_hosts.txt etc_hosts.txt.ipv6
sed -i 's/0.0.0.0 /::1 /g' etc_hosts.txt.ipv6

