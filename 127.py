#!/usr/bin/env python

from Functions import abc_hit

c_sum = 0
for c in xrange(1, 1000):
	for b in xrange(1, c):
		a = c - b	
		if abc_hit(a, b, c):
			c_sum += c
			print a, b, c
print c_sum