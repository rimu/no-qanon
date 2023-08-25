# This script converts domains.txt into a format used by Dnsmasq for IPv6.
# Usage:
#	python domains_to_dnsmasq_ipv6.py > dnsmasq_hosts.txt.ipv6

text_file = open("domains.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	print('::1 ' + line.strip() + ' www.'+ line.strip())
