#!/usr/bin/env python

from sys import argv
from Functions import *
import os
from string import digits

#############################

iname = ''			# filename input file
k = ''				# key
enc_h = True	# hex encryption disabled

# PARAMETERS
if len(argv) > 1:
	if '-i' in argv:
		iname = argv[argv.index('-i')+1]
	else:
		iname = raw_input('\nFile:\t\t')
	if '-k' in argv:
		if os.path.exists(argv[argv.index('-k')+1]):
			k = open(argv[argv.index('-k')+1], 'r').read()
		else:
			k = argv[argv.index('-k')+1]
	if '-d' in argv:
		enc_h = False 		# hex encryption enabled

while iname == '':
	iname = raw_input("\nInput file name?.. ")
	if not os.path.exists(iname):
		print "File doesn't exist!"
		iname = ''
while k == '':
	k = raw_input("\nDecription key?.. ")

if all(c in digits + 'abcdefx' for c in open(iname).read()):
	decrypt(iname, k, True)
	os.system('open ' + iname)
else:
	encrypt(iname, k, enc_h, True)