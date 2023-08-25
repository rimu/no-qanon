# this script converts dnsmasq_hosts.txt into a format used in /etc/hosts 
# usage:
#	python dnsmasq_to_etc_hosts.py > etc_hosts.txt

text_file = open("dnsmasq_hosts.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	parts = line.split(' ')
	if len(parts) == 2:
		print('0.0.0.0 ' + parts[1].strip())
	if len(parts) == 3:
		print('0.0.0.0 ' + parts[1].strip())
		print('0.0.0.0 ' + parts[2].strip())
