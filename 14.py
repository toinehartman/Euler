#!/usr/bin/env python

from Functions import isEven
maxsteps = 0
peaknum = 0
for i in xrange(1,1000001):
	n = i
	steps = 1
	while n > 1:
		if isEven(n):
			n = n/2
		else:
			n = 3*n + 1
		steps += 1
	if steps > maxsteps:
		maxsteps = steps
		peaknum = i
		print peaknum,steps
print 'Termen: ',maxsteps,' van startgetal: ',peaknum