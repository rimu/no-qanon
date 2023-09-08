# This script converts domains.txt into a match pattern format used by the uBlacklist browser extension.
# Usage:
#	python domains_to_regex.py > regex.txt
import re
text_file = open("domains.txt", "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
	print('(\.|^)' + re.escape(line.strip()) + '$')