#!/usr/bin/env python

from time import time
tic = time()
fib = 0
a = 1
b = 1
buf = 0
n = 2
while 1:
	n += 1
	fib = a + b
	# print fib
	buf = b
	b = a + b
	a = buf
	if len(str(fib)) == 1000:
		break
# print 'Term',n,'is de eerste Fibonacciterm met 1000 cijfers.'
print 'Elapsed:',time() - tic