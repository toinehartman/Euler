#!/usr/bin/env python

from Functions import isPrime
from Functions import primegen
from math import sqrt
import sys

oc = 7
while 1:
	oc += 2
	primes = primegen(oc)
	found = False
	if not isPrime(oc):
		for p in primes:
			if sqrt((oc-p)/2) == int(sqrt((oc-p)/2)):
				# print '{0} == {1} + 2 * {2}^2'.format(oc, p, int(sqrt((oc-p)/2)))
				found = True
				break
		if not found:
			print '{0} != a_prime + 2 * x^2'.format(oc)
			sys.exit('Gevonden!')