#!/usr/bin/python

import os

# os.command('ls -l')

listfile="file.txt"
destpath='../ramdisk/'

fd = open(listfile, 'r')
while True:
	rawline = fd.readline()
	if len(rawline) == 0:
		break;

	line=rawline[0:-1]

	if os.path.isdir(line) is True:
		cmd = 'mkdir -p ' + destpath + line
	elif os.path.isfile(line) is True:
		cmd = 'cp ' + line + ' ' +  destpath + line
	elif os.path.islink(line) is True:
		cmd = 'cp ' + line + ' ' +  destpath + line
	else:
		print "error! %s is unkown!" %(line)
		continue	
	os.system(cmd)
