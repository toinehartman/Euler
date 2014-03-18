#!/usr/bin/env python

from Functions import gcd
from math import sqrt

def primitive(a, b, c):
	if a%2 or b%2 or c%2:
		return (a, b, c)
	else:
		primitive(a, b, c)

opt = []
count = 0
print 'Lijst met alle mogelijke rechthoekige 3hoeken genereren'
for m in xrange(1, int(sqrt(0.5 * 15 * 10**5))):
	for n in xrange(1, m):
		if gcd(m, n) == 1 and (m - n) % 2:
			L = 2 * m * (m + n)
			for k in xrange(1, (15 * 10**5) // L + 1):
				L = k * 2 * m * (m + n)
			# a = m**2 - n**2
			# b = 2*m*n
			# c = m**2 + n**2
			# if a > b:
			# 	a, b = b, a
			# print a, b, c
				if L < 15 * 10**5:
					opt.append(L)
					# print L, m, n, k

print 'Lijst gegenereerd ({0} items/{1} distinct), checken op multipliciteit'.format(len(opt), len(set(opt)))

p = []
for length in opt:
	if opt.count(length) == 1 and length not in p:
		count += 1
		p.append(length)
		# print count

print 'Aantal unieke mogelijkheden:', count