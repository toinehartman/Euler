#!/usr/bin/env python

from decimal import *
getcontext().prec = 100

for num in xrange(1, 101):
	print Decimal((num**0.5)%1)
	# print len(Decimal((num**0.5))%1)