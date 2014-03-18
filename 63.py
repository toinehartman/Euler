#!/usr/bin/env python

c = 0
for a in xrange(1, 1000):
	for n in xrange(1, 100):
		if len(str(a**n)) == n: c += 1
print c