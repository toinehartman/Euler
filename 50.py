#!/usr/bin/env python

from Functions import primegen
from Functions import isPrime
maxcount = 0
limit = 10**6
primes = primegen(limit)

for i in xrange(0, len(primes)):
	for j in xrange(i , len(primes)):
		summ = 0
		count = 0
		for p in primes[i:j]:
			# print p,
			summ += p
			# print summ
			count += 1
		if summ < limit and isPrime(summ) and count > maxcount:
			print summ, count
			maxcount = count
		elif summ >= limit:
			break
print maxcount