#!/usr/bin/python3.6
import re
import numpy as np

ip = []
received = []
sent = []
rejects = 0

with open('log4', 'r') as f:
	for line in f:
		if re.search('blocked using dnsbl.sorbs.net', line):
			split = re.split(';', line)
			ipString = re.split(' |\[|\]', split[1])
			ip.append(ipString[4])
			received.append((re.search('from=<(\w+[\W+|.|\w])*@(\w+[.])*([\w\W])*>', split[-1])).group(0))
			sent.append((re.search('to=<(\w+[\W+|.|\w])*@(\w+[.])*([\w\W])*>', split[-1])).group(0))
			rejects += 1
	f.close()
	ipArr = np.array(ip)
	receivedArr = np.array(received)
	sentArr = np.array(sent)
	print("{} messages rejected".format(rejects))
	print("{} unique IP's".format(len(np.unique(ipArr))))
	print("{} unique from addresses".format(len(np.unique(receivedArr))))
	print("{} unique to addresses".format(len(np.unique(sentArr))))
