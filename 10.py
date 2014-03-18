#!/usr/bin/env python

from Functions import *
from time import time

tic = time()
num = 3
summ = 2
while num < 2000000:
	if isPrime(num):
		summ += num
	num += 2
print 'Sum of all primes < 2000000 is: {0}, {1} seconds'.format(summ, round(time()-tic, 4))

tic = time()
print 'Sum of all primes < 2000000 is: {0}, {1} seconds'.format(sum(prigen(2000000)), round(time()-tic, 4))