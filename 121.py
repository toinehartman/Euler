#!/usr/bin/env python

r = 1
b = 1.0
prob = 1

for i in xrange(4):
	prob *= b / (r + b)
	print prob
	r += 1
print 11.0/120
