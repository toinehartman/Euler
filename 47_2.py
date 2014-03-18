#!/usr/bin/env python

from Functions import isPrime
from Functions import pfactors

n1 = 0
n2 = 0
n3 = 0
n4 = 0
divs = []

while 1:
	n1 += 1
	divs = pfactors(n1)
	if all(isPrime(d) for d in divs) and divs != [] and len(set(divs)) == 2:
		# print n
		if n2 + 1 != n1:
			n2 = n1
		else:
			print n2, n1
			break