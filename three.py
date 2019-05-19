#!/usr/bin/python3.6
import re
import sys
from collections import Counter

receivedList = []
sentList = []

with open(str(sys.argv[1]), 'r') as f:
	for line in f:
		temp1 = re.search('from=<(\w+[.|\w])*@(\w+[.])*([\w])*>', line)
		temp2 = re.search('to=<(\w+[.|\w])*@(\w+[.])*([\w])*>', line)
		if temp1:
			receivedList.append(temp1.group(0))
		if temp2:
			sentList.append(temp2.group(0))
	received = Counter(receivedList).most_common(5)
	sent = Counter(sentList).most_common(5)
	for i in range(5):
		print(received[i])
		print(sent[i])
