#!/usr/bin/env python

target = 100
ways = [None] * (target + 1)
ways[0] = 1

for i in xrange(1, target):
	for j in xrange(i, target + 1):
		if ways[j] == None:
			ways[j] = ways[j - i]
		else:
			ways[j] += ways[j - i]
print ways[len(ways) - 1]