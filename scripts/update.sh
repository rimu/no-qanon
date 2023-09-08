#!/usr/bin/env bash

# Use this script to generate all the blocklists using the `.txt` files in the `sources` folder.
# e.g.
# ./scripts/update.sh

# Cleanup sources:
## Remove `www.` subdomains.
find ./sources -type f -name "*.txt" -exec sed -i 's/^www\.//i' {} \;
## Remove duplicates from each source file. (TO DO: keep "duplicate" line jumps and comments)
find ./sources -type f -name "*.txt" -exec bash -c '
    cat -n "$0" | sort -uk2 | sort -nk1 | cut -f2- > "$0_temp.txt";
    mv "$0_temp.txt" "$0";
' {} \;

# Combine all sources into a domains list.
find ./sources -type f -name "*.txt" -exec cat {} \; > domains.txt

# Cleanup the domain list:
## Remove comments, inline comments, spaces and empty lines.
sed -i '/^#/d; s/#.*//; s/ //g; /^ *$/d' domains.txt
## Remove duplicates.
cat -n domains.txt | sort -uk2 | sort -nk1 | cut -f2- > domains_temp.txt
mv domains_temp.txt domains.txt

# Generate blocklists:
## From the domain list.
python scripts/domains_to_hosts.py > hosts.txt
python scripts/domains_to_hosts_ipv6.py > hosts.txt.ipv6
python scripts/domains_to_regex.py > regex.txt

## For browser extensions.
python scripts/domains_to_netsane.py > netsane.txt
python scripts/domains_to_adblock.py > adblock_temp.txt
cp adblock_header.txt adblock.txt
cat adblock_temp.txt >> adblock.txt
rm adblock_temp.txt
python scripts/domains_to_ublacklist.py > ublacklist_temp.txt
cp adblock_header.txt ublacklist.txt # Currently using the same adblock header until uBlacklist implements its own header. https://github.com/iorate/ublacklist/issues/351
cat ublacklist_temp.txt >> ublacklist.txt
rm ublacklist_temp.txt