#!/usr/bin/env python

from Functions import fac

c = 0
for x in xrange(1, 10**6):
	reps = []
	s = 0
	n = x
	while n not in reps:
		# print n
		s = sum(map(fac, map(int, list(str(n)))))
		reps.append(n)
		n = s
	# if len(reps) > 60: print x
	if len(reps) == 60:
		c += 1
		print x, c
print 'Aantal met len(60)', c