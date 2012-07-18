#!/usr/bin/python

import os

# os.command('ls -l')

listfile="file.txt"

fd = open(listfile, 'r')
while True:
	rawline = fd.readline()
	if len(rawline) == 0:
		break;

	line=rawline[0:-1]

	if os.path.isfile(line) is True:
		cmd = 'arm--netbsdelf-readelf -d ' + line 
	else:
		continue	
	
	os.system('echo ======== %s =======' %line)
	os.system(cmd)
