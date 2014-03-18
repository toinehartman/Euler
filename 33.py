#!/usr/bin/env python

from fractions import Fraction

frac = []
div1 = 0.0
div2 = 0.0
prod = 1

for i in xrange(11, 100):
	for j in xrange(i+1, 100):
		if str(j)[:-1] != '0' and str(j)[1:] != '0':
			div1 = float(str(i)[:-1]) / float(str(j)[1:])
			div2 = float(i) / float(j)
			if str(i)[1:] == str(j)[:-1] and div1 == div2:
				print i, j,
				print str(i)[:-1], str(j)[1:],
				print div1, div2
				frac.append(div2)
for i in frac:
	prod *= i
print prod