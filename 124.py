#!/usr/bin/env python

from Functions import rad

E = []

print 'Radicals vinden'
for n in xrange(1, 10**5 + 1):
	E.append([rad(n), n])

print 'Sorteren'
E = sorted(E)

# print 'Lijst omkeren'
# for s in E:
# 	s[0], s[1] = s[1], s[0]
# 	# print s, E.index(s) + 1

print E[10000 - 1][1]