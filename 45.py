#!/usr/bin/env python

tri = []
pent = []
hexa = []

for n in xrange(100000):
	tri.append(n*(n+1)/2)
	pent.append(n*(3*n-1)/2)
	hexa.append(n*(2*n-1))
for num in tri:
	if num in pent and num in hexa:
		print tri.index(num), pent.index(num), hexa.index(num), num