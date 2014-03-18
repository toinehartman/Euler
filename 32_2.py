#!/usr/bin/env python

from itertools import permutations
from time import time
tic = time()
summ = 0
count = 0
prodskip = []
for x in permutations('123456789', 9):
	# print x
	for i in xrange(1, 9):
		for j in xrange(1, 9):
			if i + j <= 8:
				a = int(''.join(x[0:i]))
				b = int(''.join(x[i:i+j]))
				c = int(''.join(x[i+j:]))
				if a * b == c and a > b and c not in prodskip:
					count += 1
					summ += c
					print "{0}: {1} x {2} = {3}.. som: {4}, {5} seconden na start".format(count, a, b, c, summ, round(time()-tic, 2))
					prodskip.append(c)
print "\n{0}".format(summ)
print "Verstreken: {0} s".format(time()-tic)
