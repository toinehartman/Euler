#!/usr/bin/env python

from Functions import *
from time import *

tic = time()
count = 0
a = primegen(10**6)
for p in a:
	allprime = True
	for n in rotations(p):
		if not isPrime(n):
			allprime = False
			break
	if allprime:
		# print n
		count += 1
print 'Aantal: {0}, {1:.02f} s dmv primegen'.format(count, time()-tic)

tic = time()
count = 0
for p in prigen(10**6):
	allprime = True
	for n in rotations(p):
		if not isPrime(n):
			allprime = False
			break
	if allprime:
		# print n
		count += 1
print 'Aantal: {0}, {1:.02f} s dmv prigen en allprime = False'.format(count, time()-tic)

tic = time()
count = 0
for p in prigen(10**6):
	if all(isPrime(x) for x in rotations(p)):
		count += 1
print 'Aantal: {0}, {1:.02f} s dmv prigen en all()'.format(count, time()-tic)

tic = time()
print 'Aantal: {0}, {1:.02f} s dmv sum en all()'.format(sum(1 for p in prigen(10**6) if all(isPrime(x) for x in rotations(p))), time()-tic)
