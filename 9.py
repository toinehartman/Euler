#!/usr/bin/env python

a = 0
b = 1
c = 2
while a <=1000:
	for b in xrange(1,1001):
		c = 1000 - a - b
		if a**2 + b**2 == c**2 and a<b and b<c:
			print a,b,c
			print 'Product is ',a*b*c
			quit()
	a += 1