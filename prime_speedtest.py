#!/usr/bin/env python

from Functions import isPrime
from Tools import isprime
import time

tic = time.time()
num = 3
summ = 2
while num < 2000000:
	if isprime(num) == True:
		summ += num
	num += 2
print 'Joep:'
print 'Som van alle priemgetallen < 2000000 is: ',summ
print time.time()-tic

tic = time.time()
num = 3
summ = 2
while num < 2000000:
	if isPrime(num) == True:
		summ += num
	num += 2
print '\nToine:'
print 'Som van alle priemgetallen < 2000000 is: ',summ
print time.time()-tic