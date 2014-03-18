#!/usr/bin/env python

from Functions import *

# c = 0
# for x in xrange(1, 10**7):
# 	if len(Divisors(x)) == len(Divisors(x + 1)):
# 		c += 1
# 		if not c % 1000: print c, x
# print c

print sum(1 for x in xrange(1, 10**7) if len(Divisors(x)) == len(Divisors(x + 1)))
