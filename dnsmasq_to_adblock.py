# this script converts dnsmasq_hosts.txt into a format used by the adblock extension
# usage:
#	python dnsmasq_to_adblock.py > adblock.txt

text_file = open("dnsmasq_hosts.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	parts = line.split(' ')
	if len(parts) > 1:
		print('||' + parts[1].strip() + '^')
