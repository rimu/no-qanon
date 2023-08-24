# this script converts dnsmasq_hosts.txt into a format used by the adblock extension
# usage:
#	python dnsmasq_to_adblock.py > adblock.txt

text_file = open("domains.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	print('||' + line.strip() + '^')
