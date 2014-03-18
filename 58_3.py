#!/usr/bin/env python

from Functions import *

n = 1
r = [0.0, 1.0]
while r[0]/r[1] > 0.1 or r[0] == 0:
	n += 2
	r[1] += 4
	for a in xrange(1, 4):
		if isPrime(n**2-a*(n-1)):
			r[0] += 1
	# if not (r[1]-1)%100:
		# print n, r[0]/r[1]
print n, r[0]/r[1], r[0], r[1]