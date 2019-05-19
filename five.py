#!/usr/bin/python3.6
import re
import sys

with open(str(sys.argv[1]), 'r') as f:
	lines = f.readlines()
	f.close()
with open(str(sys.argv[1]), 'w') as f:
	for line in lines:
		i = 2
		write = True
		for i in range(len(sys.argv)):
			if re.search(sys.argv[i], line):
				write = False
		if write:
			f.write(line)
	f.close()
