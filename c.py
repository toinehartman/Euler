#!/usr/bin/env python

from sys import argv
from os import system
import subprocess

m = False
args = []

if len(argv) < 2:
	print 'Argumenten nodig!'

else:
	if '-m' in argv:
		m = True
		files = [f for f in argv[argv.index('-m') + 1:]]
	else:
		ifile = argv[1]
		ofile = argv[1][:-2]
	if '--args' in argv:
		args = [arg for arg in argv[argv.index('--args') + 1:]]
	# print '{0} --> {1}'.format(ifile, ofile)
	print 'm = {0}, ifile = {1}, ofile = {2}'.format(str(m), ifile, ofile)
	if not m:
		if system('gcc {0} -o {1} -ansi -pedantic -lm -Wall'.format(ifile, ofile)) == 0:
			print 'Succes, will run now!\n'
			system('./{0} {1}'.format(ofile, ' '.join(args)))
	else:
		if system('gcc -c {0}'.format(' '.join(files))) == 0:
			print 'Succes, will now compile object files and run!\n'
			if system('gcc -o program *.o') == 0:
				system('./{0} {1}'.format('program', ' '.join(args)))
