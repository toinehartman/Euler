#!/usr/bin/env python

from Functions import isDivisible
trinum = 0
count = 0
div = 0
while div <= 500:
	trinum += count + 1
	count += 1
	div = 0
	for d in xrange(1, int(trinum**0.5)):
		# print d
		# raw_input('...')
		if isDivisible(trinum, d):
			div += 2
	# print '{0} heeft {1} delers.'.format(trinum, div)
print 'Eerste "triangle number" met meer dan 500 delers: {0}.\n{1} delers.'.format(trinum, div)