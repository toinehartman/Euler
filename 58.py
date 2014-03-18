#!/usr/bin/env python

from Functions import isPrime
from time import sleep

def spipri(dim):
	num = 1
	yield num
	while 1:
		dim += 2
		for i in xrange(1, (dim-1)/2+1):
			for x in xrange(1, 5):
				num += i * 2
				yield num
		yield dim**2
d = 5
while 1:
	d += 2
	for a in spipri(d):
		print a
		sleep(1)