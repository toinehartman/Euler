#!/usr/bin/env python

from Functions import combicount
count = 0
for n in xrange(1, 101):
	for r in xrange(1, n+1):
		if combicount(n, r) > 10**6:
			count +=1
print count