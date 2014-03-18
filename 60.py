#!/usr/bin/env python

from Functions import *
from itertools import *

print 'Lijst primes maken'
primes = [x for x in primesix(1000)]
for a in primes:
	for b in primes:
		for c in primes:
			for d in primes:
				if all(isPrime(int(''.join(str(v) for v in p) for p in combinations([a, b, c, d], 2))):
					print a, b, c, d