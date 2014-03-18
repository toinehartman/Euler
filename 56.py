#!/usr/bin/env python

maxx = 0
for a in xrange(1, 100):
	for b in xrange(1, 100):
		summ = 0
		num = str(a**b)
		for d in num:
			summ += int(d)
		if summ > maxx:
			maxx = summ
print maxx