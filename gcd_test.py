#!/usr/bin/env python

from Functions import *
from time import *

tic = time()
for a in xrange(1, 1000):
	for b in xrange(1, 1000):
		x = gcd(a, b)
print 'GCD van PinC, iteratief: {0} s'.format(round(time() - tic, 4))

tic = time()
for a in xrange(1, 1000):
	for b in xrange(1, 1000):
		x = bit_gcd(a, b)
print 'GCD van Stein: {0} s'.format(round(time() - tic, 4))

tic = time()
for a in xrange(1, 1000):
	for b in xrange(1, 1000):
		x = euc_gcd(a, b)
print 'GCD van Euclides: {0} s'.format(round(time() - tic, 4))

tic = time()
for a in xrange(1, 1000):
	for b in xrange(1, 1000):
		x = rec_gcd(a, b)
print 'GCD van PinC, recursief: {0} s'.format(round(time() - tic, 4))