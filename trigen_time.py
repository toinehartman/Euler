#!/usr/bin/env python

import time
import random
from os import system
from sys import argv
from sys import stdout

def trigen_time(l):
		bytes = 1.5*l**2
		if bytes >= 10**9:
			size = '{0:.1f} GB'.format(bytes/10**9)
		elif bytes >= 10**6:
			size = '{0:.1f} MB'.format(bytes/10**6)
		elif bytes >= 10**3:
			size = '{0:.1f} KB'.format(bytes/10**3)
		elif bytes >= 0:
			size = '{0:.1f} B'.format(bytes)

		tic = time.time()

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
		tijd = time.time()-tic
		system('rm /Users/Toine/Desktop/{0}'.format(filename))
		return [l, bytes, round(tijd, 2)]

if len(argv) == 1:
	print '''-l <spatie> [lengte] voor aantal regels\n
	-o voor openen in texteditor\n'''
elif '-l' in argv:
	b = int(argv[argv.index('-l') + 1])
	e = int(argv[argv.index('-l') + 2])
	s = int(argv[argv.index('-l') + 3])

system('date')
for i in xrange(b, e, s):
	print ' '.join(map(str, trigen_time(i)))