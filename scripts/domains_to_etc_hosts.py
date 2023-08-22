# this script converts dnsmasq_hosts.txt into a format used in /etc/hosts 
# usage:
#	python dnsmasq_to_etc_hosts.py > etc_hosts.txt

text_file = open("domains.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
		print('0.0.0.0 ' + line.strip())
		print('0.0.0.0 www.' + line.strip())
