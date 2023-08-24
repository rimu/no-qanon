# No-QAnon
A blocklist of QAnon, conspiracy, fake news, fascist and racist websites.

Distributed under the [anti-fascist licence](https://github.com/rimu/no-qanon/blob/master/LICENSE.txt).

## Hosts format

[Blocklist in Hosts format](https://raw.githubusercontent.com/rimu/no-qanon/master/etc_hosts.txt) to use in a `/etc/hosts` file or pihole.

[IPV6 version](https://raw.githubusercontent.com/rimu/no-qanon/master/etc_hosts.txt.ipv6).

### How to install on a Windows computer
[See these instructions](https://github.com/yui-konnu/qanon-block-guide).

### How to install on a PiHole
[See these instructions](https://www.reddit.com/r/QAnonCasualties/comments/wekhem/how_to_use_pihole_to_block_q_related_websites/). Use the [etc_hosts.txt](https://raw.githubusercontent.com/rimu/no-qanon/master/etc_hosts.txt) version of the No QAnon list with a PiHole.

## Dnsmasq format

[Blocklist in Dnsmasq format](https://raw.githubusercontent.com/rimu/no-qanon/master/dnsmasq_hosts.txt) to use with the dnsmasq DNS server software.

[IPV6 version](https://raw.githubusercontent.com/rimu/no-qanon/master/dnsmasq_hosts.txt.ipv6).

## Browser extensions

### AdBlock Plus syntax
[Blocklist in AdBlock format](https://raw.githubusercontent.com/rimu/no-qanon/master/adblock.txt) to use with an adblocker ([uBlock Origin](https://ublockorigin.com), [Adguard](https://adguard.com)…) or Adguard Home.

[Click here to subscribe.](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/rimu/no-qanon/master/adblock.txt&title=No-QAnon)

### uBlacklist syntax
[Blocklist in uBlacklist format](https://raw.githubusercontent.com/rimu/no-qanon/master/ublacklist.txt) to use with [uBlacklist](https://github.com/iorate/ublacklist).\
[Click here to subscribe.](https://iorate.github.io/ublacklist/subscribe?name=No-QAnon&url=https://raw.githubusercontent.com/rimu/no-qanon/master/ublacklist.txt)

### Domains list
[Domains list format](https://raw.githubusercontent.com/rimu/no-qanon/master/domains.txt) to use with [Search Engine Spam Blocker](https://github.com/no-cmyk/Search-Engine-Spam-Blocker).

## How to contribute
Clone this repository and append new domains at the end of the `domains.txt` file.

For the `https://www.example.com` website, add `example.com`.

Then from the command line run `./update_from_domain "some description"` to automatically generate new versions of all the blocklists and create a git commit. At the end of the script it will attempt to push the commit up to the original repository, which might not work. Do whatever you normally do to create a Pull Request and we will approve it within a couple of days.

## Other useful lists

[Jmdugan Blocklists](https://github.com/jmdugan/blocklists/tree/master/corporations) and consider blocking Twitter, YouTube and Facebook since they publish to many fakenews.

[Antifa-n Blocklist](https://github.com/antifa-n/pihole/blob/master/blocklist.txt) is a great blocklist also, focused more on fascist sites.

[Bypass Methods Blocklist](https://github.com/nextdns/metadata/blob/master/parentalcontrol/bypass-methods) can be used to block bypass methods - VPNs, proxies, DNS, etc.
