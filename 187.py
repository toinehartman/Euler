#!/usr/bin/env python

from Functions import *

ints = []
c = 0
lim = 30

for a, b in prigen(lim / 2):
	if b > a and a * b < lim:
		c += 1
		print '{0}, {1} ({2} x {3})'.format(c, a * b, a, b)
	else: break
print c