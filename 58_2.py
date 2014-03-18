#!/usr/bin/env python

from Functions import isPrime

ratio = 0.62
dim = 5
while ratio > 0.10:
	dim += 2
	d = []
	num = 1
	for i in xrange(1, (dim-1)/2+1):
		for x in xrange(1, 5):
			d.append(num)
			num += i * 2
	d.append(dim**2)

	r = [0, 0]
	for n in d:
		if isPrime(n):
			r[0] += 1
		r[1] += 1
	ratio = float(r[0])/float(r[1])
	# print dim, ratio
print dim, r