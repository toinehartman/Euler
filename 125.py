#!/usr/bin/env python

from Functions import *

# s = 0
# ls = []

# print 'Lijst maken'
# for n in xrange(2, 1000):
# 	if isPalindrome(n):
# 		ls.append(n)

sq_ls = []
for a in xrange(1, 502):
	sq = 0
	while sq + a**2 < 1000:
		sq += a**2
		sq_ls.append(sq)

summ = 0
for s in sq_ls:
	if isPalindrome(s):
		print s
		summ += s
print 'Som:', summ