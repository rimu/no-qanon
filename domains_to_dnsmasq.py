# this script converts dnsmasq_hosts.txt into a match pattern format used by the uBlacklist extension
# usage:
#	python dnsmasq_to_ublacklist.py > ublacklist.txt

text_file = open("domains.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	print('0.0.0.0 ' + line.strip() + ' www.'+ line.strip())
