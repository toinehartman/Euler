#!/usr/bin/env python

from time import time
import random
from os import system
from sys import argv

# system('clear')
print ''
system('date')
print ''
if len(argv) == 1:
	print '''-l <spatie> [lengte] voor aantal regels\n
	-o voor openen in texteditor\n'''
else:
	if '-l' in argv:
		l = int(argv[argv.index('-l') + 1])

	bytes = 1.5*l**2
	if bytes >= 10**9:
		print 'Grootte: {0:.1f} GB.'.format(bytes/10**9)
	elif bytes >= 10**6:
		print 'Grootte: {0:.1f} MB.'.format(bytes/10**6)
	elif bytes >= 10**3:
		print 'Grootte: {0:.1f} KB.'.format(bytes/10**3)
	elif bytes >= 0:
		print 'Grootte: {0:.1f} B.'.format(bytes)

	tic = time()

	filename = 'trigen2_{0}.txt'.format(l)
	f = open('/Users/Toine/Desktop/{0}'.format(filename), 'w')
	for i in xrange(0, l + 1):
		for n in xrange(0, i):
			f.write(str(random.randrange(0, 100)).zfill(2))
			if n == i - 1 and i != l:
				f.write('\n')
			elif n != i - 1:
				f.write(' ')
	f.close()
	print 'Verstreken tijd: {0:.2f} s'.format(round(time() - tic), 2)
	if '-o' in argv:
		system('open /Users/Toine/Desktop/{0}'.format(filename))
	print ''