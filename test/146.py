#!/usr/bin/env python

from Functions import isPrime
from time import time

terms = [1,3,7,9,13,27]
summ = 0
possPrimes = []
tic = time()

for n in xrange(0, 10**6, 2):
	streak = True
	possPrimes = []
	for t in terms:
		possPrimes.append(n**2 + t)
	# print n
	for i in xrange(0, 5):
		if not streak:
			continue
		for a in xrange(int(possPrimes[i]), int(possPrimes[i+1])):
			if isPrime(a):
				streak = False
				continue
	if streak:
		# print n
		summ += n
print possPrimes
print summ
print '{0} s'.format(round(time() - tic, 3))


# for n in xrange(0,1000000,2):
# 	kloppend = True
# 	for i in terms:
# 		if not isPrime(n**2+i):
# 			kloppend = False
# 			break
# 	if kloppend:
# 		summ += n
# 		print n
# print 'Som:',summ