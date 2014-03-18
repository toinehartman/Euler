#!/usr/bin/env python

from Functions import *
from time import time

lim = 10**6


tic = time()
num = 0

primes = [x for x in prigen(lim)]
for d in xrange(2, lim + 1):
	if d in primes:
		num += d - 1
	else:
		num += 1
		for x in xrange(2, d):
			if not d % x:
				num += 1
	if not d % 1000:
		print(d)

print(num), round(time() - tic, 4)

tic = time()
num = 0

for d in xrange(2, lim + 1):
	if isPrime(d):
		num += d - 1
	else:
		num += 1
		for x in xrange(2, d):
			if not d % x:
				num += 1
	# if not d % 1000:
	# 	print(d)

print num, round(time() - tic, 4)