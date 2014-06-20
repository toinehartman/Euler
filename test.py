#!/usr/bin/env python

from Functions import isDivisible
n = 20*19*17*13*11*7*3
while 1:
	if isDivisible(n,12) == True & isDivisible(n,14) == True & isDivisible(n,15) == True & isDivisible(n,16) == True & isDivisible(n,18) == True:
		print 'Deelbaar door alle getallen van 1 t/m 20 zonder rest:', n
		break
	# print n,
	n += 20*19*17*13*11*7*3