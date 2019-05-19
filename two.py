#!/usr/bin/python3.6
import re
from statistics import mode
from collections import Counter

unknowns = []
knowns = []

with open('log2', 'r') as f:
	for line in f:
		if  (re.search(' connect from ', line) and re.search('unknown', line)):
			line = re.split(r'\[|\]', line)
			unknowns.append(line[-2])
		elif re.search(' connect from ', line):
			line = re.split(r'\[|\]', line)
			knowns.append(line[-2])
	numKnown = len(knowns)
	numUnknown = len(unknowns)
	commonKnown = mode(knowns)
	commonUnknown = mode(unknowns)
	numCom = knowns.count(commonKnown)
	numUCom = unknowns.count(commonUnknown)
	print("Total Unknown connections: {} - [{}] for {} connections".format(numUnknown, commonUnknown, numUCom))
	print("Total Known connections: {} - [{}] for {} connections".format(numKnown, commonKnown, numCom))
	f.close()
