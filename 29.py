#!/usr/bin/env python

p = []
for a in xrange(2, 101):
	for b in xrange(2, 101):
		# print a, b
		p.append(a**b)
print len(set(p))

print len(set(a**b for a in xrange(2, 101) for b in xrange(2, 101)))
