# This script converts domains.txt into a format used in /etc/hosts.
# Usage:
#	python domains_to_etc_hosts.py > etc_hosts.txt

text_file = open("domains.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	print('"*://*.' + line.strip() + '/*",')

