#!/usr/bin/env python

from math import sqrt

tot = 0
for L in xrange(1500000):
	count = 0
	for a in xrange(L):
		for b in xrange(a, L):
			c = sqrt(a**2 + b**2)
			if not c%1 and a != 0 and b != 0 and a + b + c == L:
				count += 1
	if count == 1:
		print L
		tot += 1
print tot