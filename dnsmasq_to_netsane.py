# this script converts dnsmasq_hosts.txt into a format used in /etc/hosts 
# usage:
#	python dnsmasq_to_etc_hosts.py > etc_hosts.txt

text_file = open("dnsmasq_hosts.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	parts = line.split(' ')
	if len(parts) == 2 or len(parts) == 3:
		print('*://*.' + parts[1].strip() + '/*')

