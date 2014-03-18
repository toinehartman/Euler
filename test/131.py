#!/usr/bin/env python

from Functions import *

c = 0
while c < 4:
	for n in xrange(100):
		if any(not ((n**3 + p * n**2)**(1.0/3))%1 for p in prigen(100)):
			print n, p