#!/usr/bin/env python

from itertools import *

ops = ['add'] * 3 + ['sub'] * 3 + ['mul'] * 3 + ['div'] * 3
nums = [1, 2, 3, 4]

results = []
for c in set(combinations(ops, 3)):
	for n in set(permutations(nums)):
		print n
		print c
		s = n[0]
		for i in xrange(len(c)):
			if c[i] == 'add':
				s += n[i+1]
			elif c[i] == 'sub':
				s -= n[i+1]
			elif c[i] == 'mul':
				s *= n[i+1]
			elif c[i] == 'div':
				s /= n[i+1]
			if not s in results:
				results.append(s)
print len(results), sorted(results)