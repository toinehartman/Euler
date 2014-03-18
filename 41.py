#!/usr/bin/env python

from Functions import isPrime
from itertools import permutations
from string import digits

plist = []
l = 0
for i in xrange(9, 0, -1):
	perms = permutations(digits[1:i+1])
	for p in perms:
		perm = ",".join(p).replace(",", "")
		perm = int(perm)
		if isPrime(perm):
			if perm > l:
				l = perm
			print perm
print l