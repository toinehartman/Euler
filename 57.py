#!/usr/bin/env python

def root(i):
	i = float(i)
	if i == 1:
		return 1.0+1.0/2.0
	else:
		return 1.0+1.0/(1.0+root(i-1))

def n(i):
	if i == 1:
		return 3
	else:
		return n(i-1) + 2*d(i-1)

def d(i):
	if i == 1:
		return 2
	else:
		return n(i) - d(i-1)

count = 0
num = 3
den = 2

for i in xrange(1, 1001):
	num += 2 * den
	den = num - den
	if len(str(num)) > len(str(den)):
		count += 1
print count