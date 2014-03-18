#!/usr/bin/env python

from Functions import *

target = 10
primes = primegen(target + 1)
ways = [None] * (target + 1)
ways[0] = 1
print primes
print ways

for i in xrange(len(primes)):
	for j in xrange(primes[i], target + 1):
		if ways[j] == None:
			ways[j] = ways[j - primes[i]]
		else:
			ways[j] += ways[j - primes[i]]
print ways[len(ways) - 1]