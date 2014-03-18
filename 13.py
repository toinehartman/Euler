#!/usr/bin/env python

from time import time
nums = open('num13.txt', 'r')
list = []
tic = time()
s = 0
for line in open('num13.txt'):
	if line.strip():
		s += int(line)
print str(s)[0:10], round(time()-tic, 4), 's'

s = 0
tic = time()
for i in xrange(0,100):
	s += int(nums.readline())
print str(s)[0:10], round(time()-tic, 4), 's'
nums.close()