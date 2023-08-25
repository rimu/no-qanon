# This script converts domains.txt into a format used by Dnsmasq.
# Usage:
#	python domains_to_dnsmasq.py > dnsmasq_hosts.txt

text_file = open("domains.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	print('0.0.0.0 ' + line.strip() + ' www.'+ line.strip())
