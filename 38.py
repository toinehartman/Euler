#!/usr/bin/env python

from Functions import isPandigital

p_max = 0
for n in xrange(98765):
	p = ''
	x = 1
	while len(p) < 9:
		p += str(x*n)
		x += 1
	if len(p) == 9 and isPandigital(p):
		# print p
		if p > p_max:
			p_max = p
			print p_max
print 'Hoogste = {0}'.format(p_max)