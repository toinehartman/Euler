#!/usr/bin/env python

r_max_sum = 0
for a in xrange(3, 1001):
	r_max = 0
	for n in xrange(1, 1000):
		r = ((a - 1)**n + (a + 1)**n) % a**2
		if r > r_max:
			r_max = r
	print a, r_max
	r_max_sum += r_max
print r_max_sum