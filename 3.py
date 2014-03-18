#!/usr/bin/env python

from Functions import isPrime
from math import sqrt
from time import time

number = 600851475143
tic = time()
finished = False
for i in xrange(2, int(sqrt(number))+1):
	if finished:
		break
	else:
		# print "Noemer: %d" % (i)
		while  1:
			if isPrime(number) == True:
				# print "Is priemgetal!"
				finished = True
				print number
				break
			elif number%i == 0:
				number /= i
			else:
				break
print 'Verstreken:',time() - tic,'s'
