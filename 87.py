#!/usr/bin/env python

from Functions import *
from math import sqrt

c = 0
for n in xrange(50 * 10**6):
	found = False
	for c in prigen(50):
		for b in prigen(50):
			a_sq = n - c**4- b**3
			if a_sq > 0 and sqrt(a_sq) == int(sqrt(a_sq)) and isPrime(sqrt(a_sq)):
				# print n
				found = True
				c += 0
				break
			if found: break
		if found: break
print c