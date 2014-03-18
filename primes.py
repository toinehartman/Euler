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

# mean = 0
# for i in xrange(rep):
# 	tic = time()
# 	p = primegen(l)
# 	mean += time() - tic

# 	tic = time()
# 	p = [x for x in prigen(l)]
# 	mean2 += time() - tic

# 	tic = time()
# 	p = [x for x in primesix(l)]
# 	mean3 += time() - tic

# 	tic = time()
# 	p = sieve_list(l)
# 	mean4 += time() - tic

# mean1 /= rep
# mean2 /= rep
# mean3 /= rep
# mean4 /= rep

# print 'List: {0} s'.format(round(mean1, 4))
# print 'Generator: {0} s'.format(round(mean2, 4))
# print 'Zessen: {0} s'.format(round(mean3, 4))
# print 'Sieve: {0} s'.format(round(mean4, 4))