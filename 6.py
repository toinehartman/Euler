#!/usr/bin/env python

sumOfSquare = 0
squareOfSum = 0
summation = 0
dif = 0
for i in xrange(1,101):
	sumOfSquare += i**2
	summation += i
	print i
	print sumOfSquare
	print summation
squareOfSum = summation**2
print squareOfSum
dif = sumOfSquare - squareOfSum
print dif