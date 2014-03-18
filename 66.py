#!/usr/bin/env python

from Functions import *
from sympy import *

lim = 8
D = [x for x in xrange(2, lim + 1) if not sqrt(x) == int(sqrt(x))]
if len(D) < 20: print D

max_x = 0
for d in D:
	found = False
	for x in xrange(1, lim * 100):
		for y in xrange(1, lim * 100):
			if x**2 - d * y**2 == 1:
				# print '{0}**2 - {1}x{2}**2 = 1'.format(x, d, y)
				found = True
				if x > max_x:
					max_x = x
				print max_x, 'D:', d, 'x:', x, 'y:', y, 'x/y:', float(x)/float(y)
				break
		if found: break
	if not found: print 'OHOH', d
print max_x