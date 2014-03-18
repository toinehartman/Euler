#!/usr/bin/env python

from Functions import primegen, isPrime

lim = 10**6

fractions = []
for d in xrange(2, lim + 1):
	if isPrime(d):
		for n in xrange(1, d):
			fractions.append([n, d])
	else:
		for p in [1] + primegen(d - 1):
			if d % p or p == 1:
				fractions.append([p, d])

# s = False
# while not s:
# 	for i in xrange(1, len(fractions)):
# 		if float(fractions[i][0])/float(fractions[i][1]) < float(fractions[i - 1][0])/float(fractions[i - 1][1]):
# 			fractions[i], fractions[i - 1] = fractions[i - 1], fractions[i]
# 			break
# 		s = True
			
print(len(fractions))