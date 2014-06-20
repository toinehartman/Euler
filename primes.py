#!/usr/bin/env python

from time import time
from Functions import *
import itertools

l = 10**3
rep = 1000
f = rep * l

mean = 0
for i in xrange(rep):
	tic = time()
	p = primegen(l)
	mean += time() - tic

mean /= f
print 'primegen: {0} us per prime'.format(round(mean * 10**6, 4))

mean = 0
for i in xrange(rep):
	tic = time()
	p = [x for x in prigen(l)]
	mean += time() - tic

mean /= f
print 'prigen: {0} us per prime'.format(round(mean * 10**6, 4))

mean = 0
for i in xrange(rep):
	tic = time()
	p = sieve_list(l)
	mean += time() - tic

mean /= f
print 'sieve_list: {0} us per prime'.format(round(mean * 10**6, 4))

mean = 0
for i in xrange(rep):
	tic = time()
	p = [x for x in primesix(l)]
	mean += time() - tic

mean /= f
print 'primesix: {0} us per prime'.format(round(mean * 10**6, 4))
