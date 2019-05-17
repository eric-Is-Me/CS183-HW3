#!/usr/bin/python3.6
import re
s = "mar 1 00:30:03 avas postfix/smtpd[2610]: connect from unknown[208.37.192.234]"
out = re.split(r'\[|\]', s)
print(out)

with open('log2', 'r') as f:
	for line in f:
		if  (re.search(' connect from ', line) and re.search('unknown', line)):
	
