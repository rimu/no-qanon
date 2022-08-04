# QAnon, Conspiracy, Fakenews and Racist Blocklists

## IPV4 Version
[Blocklist in Hosts format](https://raw.githubusercontent.com/rimu/no-qanon/master/etc_hosts.txt) to use in a /etc/hosts file or pihole.\
[Blocklist in Dnsmasq format](https://raw.githubusercontent.com/rimu/no-qanon/master/dnsmasq_hosts.txt) to use with the dnsmasq DNS server software.

## IPV6 Version
[Blocklist in Hosts format](https://raw.githubusercontent.com/rimu/no-qanon/master/etc_hosts.txt.ipv6) to use in a /etc/hosts file or pihole.\
[Blocklist in Dnsmasq format](https://raw.githubusercontent.com/rimu/no-qanon/master/dnsmasq_hosts.txt.ipv6) to use with the dnsmasq DNS server software.

## AdBlock Plus syntax
[Blocklist in AdBlock format](https://raw.githubusercontent.com/rimu/no-qanon/master/adblock.txt) to use with Adblocker (uBlock Origin, Adguard) or Adguard Home.

## Other useful lists

[Jmdugan Blocklists](https://github.com/jmdugan/blocklists/tree/master/corporations) and consider blocking Twitter, YouTube and Facebook since they publish to many fakenews.\
[Antifa-n Blocklist](https://github.com/antifa-n/pihole/blob/master/blocklist.txt) is a great blocklist also, focused more on fascist sites.\
[Bypass Methods Blocklist](https://github.com/nextdns/metadata/blob/master/parentalcontrol/bypass-methods) can be used to block bypass methods - VPNs, proxies, DNS, etc.

## How to install on a Windows computer
[See these instructions](https://github.com/yui-konnu/qanon-block-guide)

## How to install on a PiHole
[See these instructions](https://www.reddit.com/r/QAnonCasualties/comments/wekhem/how_to_use_pihole_to_block_q_related_websites/). Use the [etc_hosts.txt](https://raw.githubusercontent.com/rimu/no-qanon/master/etc_hosts.txt) version of no-qanon with a PiHole.

## How to contribute
Clone this repository to your computer.

Append new websites to dnsmasq_hosts.txt in this format:

`0.0.0.0 website.com www.website.com`

Then from the command line run `./update "some description"` to automatically copy the new websites to other formats stored in etc_hosts.txt, etc and create a git commit. At the end of the script it will attempt to push the commit up to the original repository, which might not work. Do whatever you normally do to create a Pull Request and we will approve it within a couple of days.
