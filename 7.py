#!/usr/bin/env python

from Functions import isPrime
position = 1
number = 1
while position < 10001:
	number += 2
	if isPrime(number) == True:
		print number,' positie: ',position
		position += 1
print 'Het ',position,'ste priemgetal is ',number