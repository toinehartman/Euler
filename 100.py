#!/usr/bin/env python

from math import sqrt

# for b in xrange(1, 10**12):
# 	for r in xrange(1, b):
# 		if float(b*(b - 1))/float((b + r)*(b + r - 1)) == 0.5:
# 			print b, r, float(b)/float(r)
# 		if b + r > 10**12:
# 			break

for b in xrange(707 * 10**9, 10**12):
	for r in xrange(int(2.4 * b), int(2.5 * b)):
		if float(b*(b - 1))/float((b + r)*(b + r - 1)) == 0.5:
			print b, r, float(b)/float(r)