# No-QAnon
A blocklist of QAnon, conspiracy, fake news, fascist and racist websites.

Distributed under the [anti-fascist licence](https://github.com/rimu/no-qanon/blob/master/LICENSE.txt).

## Hosts format

[Blocklist in Hosts format](https://raw.githubusercontent.com/rimu/no-qanon/master/hosts.txt) to use in a [hosts](https://en.wikipedia.org/wiki/Hosts_(file)) file or PiHole.

[IPV6 version](https://raw.githubusercontent.com/rimu/no-qanon/master/hosts.txt.ipv6).

- [Instructions to install on a Windows computer.](https://github.com/yui-konnu/qanon-block-guide)

- [Instructions to install on a PiHole.](https://www.reddit.com/r/QAnonCasualties/comments/wekhem/how_to_use_pihole_to_block_q_related_websites/)

## Dnsmasq format

[Blocklist in Dnsmasq format](https://raw.githubusercontent.com/rimu/no-qanon/master/dnsmasq_hosts.txt) to use with the [Dnsmasq](https://thekelleys.org.uk/dnsmasq/doc.html) DNS server software.

[IPV6 version](https://raw.githubusercontent.com/rimu/no-qanon/master/dnsmasq_hosts.txt.ipv6).

## Netsane format

[Blocklist in Netsane format](https://raw.githubusercontent.com/rimu/no-qanon/master/netsane.txt) to use with the [Netsane](https://github.com/rgregory/netsane) software.

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

Then, when you push your changes to the `master` branch, GitHub actions should kick in and automatically generate new versions of the blocklists.

Should you want to generate them yourself, you can run the `./update` script (prerequisites : bash, python, git).

## Other useful lists

[Jmdugan Blocklists](https://github.com/jmdugan/blocklists/tree/master/corporations) and consider blocking Twitter, YouTube and Facebook since they publish to many fakenews.

[Antifa-n Blocklist](https://github.com/antifa-n/pihole/blob/master/blocklist.txt) is a great blocklist also, focused more on fascist sites.

[Bypass Methods Blocklist](https://github.com/nextdns/metadata/blob/master/parentalcontrol/bypass-methods) can be used to block bypass methods - VPNs, proxies, DNS, etc.
