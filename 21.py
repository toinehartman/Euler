#!/usr/bin/env python

from Functions import isDivisible
from time import time
tic = time()
amicSum = 0
def d(p):
	summ = 0
	for n in xrange(1,p):
		if isDivisible(p,n):
			summ += n
	return summ
# print d(input('Getal: '))
for i in xrange(1, 10000):
	if i == d(d(i)) and i != d(i):
		print i
		amicSum += i
print 'Som van alle "amicable numbers" < 10000:',amicSum
print 'Verstreken tijd:',time() - tic, 's'