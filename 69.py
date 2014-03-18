#!/usr/bin/env python

from Functions import *
from time import time

tic = time()
max_ratio = 0
for n in xrange(2, 10**6 + 1):
	phi = 0
	if isPrime(n):
		phi = n - 1
	elif not n%2:
		for r in xrange(1, n, 2):
			if gcd(n, r) == 1:
				phi += 1
	else:
		for r in xrange(1, n):
			if gcd(n, r) == 1:
				phi += 1

	ratio = float(n) / float(phi)
	if ratio > max_ratio:
		max_ratio = ratio
		print n, phi, ratio, round(time()-tic, 4)