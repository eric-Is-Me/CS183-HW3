#!/usr/bin/python3.6
import sys
import re

rejects = 0
quarantines = 0
minute = "00"
thisLine = []

with open(str(sys.argv[1]), 'r') as f:
	for line in f:
		thisLine = re.split(':|,|->| ', line)
		if minute != thisLine[4]:
			outFile = open("hourlyInfo.txt", 'a')
			outFile.write("Mar 1 00:" + str(minute) + " [postfix rejects:" + str(rejects) + "] [amavis quarantines:" + str(quarantines) + "]\n")
			rejects = 0
			quarantines = 0
		minute = thisLine[4]
		if "reject" in line:
			rejects += 1
		if "quarantine" in line:
			quarantines += 1
outFile.close()
f.close()
