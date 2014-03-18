#!/usr/bin/env python

from Functions import isEven
a = 0
b = 1
buf = b
som = 0
for i in xrange(40):
	#print a
	#print b
	fib = a + b
	buf = b
	b = a + b
	a = buf
	if fib > 4000000:
		break
	if isEven(fib) == True:
		print fib,",",
		som += fib
	#print a
	#print b
print " Som van even Fibonacci-getallen kleiner dan 4000000: ",som