#!/usr/bin/env python

from Functions import bouncy

num = 0
b = 0
for num in xrange(10**10 + 1):
	if not bouncy(num):
		b += 1
print b, num