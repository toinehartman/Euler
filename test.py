#!/usr/bin/env python

from Functions import *

lim = 1000
c = 0

for a in xrange(1, lim):
	for b in xrange(a, lim):
		if gcd(a, b) == 1:
			c += 1
print c
