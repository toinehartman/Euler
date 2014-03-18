#!/usr/bin/env python

from time import time
from random import randint
import os

lines = list()
rowstr = str()
print '\n',
l = int(raw_input('Hoeveel regels?...   '))
print 'Verwacht: {0} s'.format(0.0005 * l**2 - (0.0086 * l))
tic = time()
print ''
print 'Driehoek van {0} rijen creeren...'.format(l)
for i in xrange(0,l+1):
	row = list()
	for j in xrange(0,i):
		row.append(str(randint(0, 99)).zfill(2))
		rowstr = ' '.join(map(str, row))
	lines.append(rowstr)
	lines = filter(None, lines)
	linesstr = '\n'.join(map(str, lines))
print 'Klaar!'
print ''
print 'Schrijven naar bestand...'

filename = 'trigen{0}.txt'.format(l)

f = open(filename, 'w')

f.writelines(linesstr)

print 'Klaar!'
print ''
print 'Tijd: {0:.2f} s'.format(round(float(time()-tic),2))
# print datetime.timedelta(seconds=time()-tic)
print ''
os.system("open {0}".format(filename))