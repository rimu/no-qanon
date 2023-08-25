# this script converts dnsmasq_hosts.txt into a match pattern format used by the uBlacklist extension
# usage:
#	python dnsmasq_to_ublacklist.py > ublacklist.txt

text_file = open("dnsmasq_hosts.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	parts = line.split(' ')
	if len(parts) > 1:
		print('*://*.' + parts[1].strip() + '/*')
