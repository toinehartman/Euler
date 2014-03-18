#!/usr/bin/env python

from itertools import permutations

cubes = [''.join(sorted(list(str(x**3)))) for x in xrange(1, 10**4)]

for a in cubes:
	c = 0
	i = cubes.index(a)
	j = i + 1
	for b in cubes[i:]:
		if a == b:
			i = cubes.index(b)
			c += 1
	if c == 5:
		print j, j**3, a
		break