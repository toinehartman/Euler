#!/usr/bin/env python

from math import sqrt

def isSquare(a):
	return not sqrt(a)%1

lim = 100000
for z in xrange(1, lim):
	for y in xrange(z + 1, lim):
		for x in xrange(y + 1, lim):
			if isSquare(x+y) and isSquare(x-y) and isSquare(x+z) and isSquare(x-z) and isSquare(y+z) and isSquare(y-z):
				print x, y, z, x + y + z