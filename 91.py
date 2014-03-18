#!/usr/bin/env python

from math import sqrt

c = 0
n = 50
coords = []
for x in xrange(n+1):
	for y in xrange(n+1):
				if x != 0 or y != 0:
					if not [x, y] in coords:
						coords.append([x, y])
# print coords

for A in coords:
	for B in coords[coords.index(A) + 1:]:
		l_A = A[0]**2 + A[1]**2
		l_B = B[0]**2 + B[1]**2
		l_C = (A[0]-B[0])**2 + (A[1]-B[1])**2
		# print l_A, l_B, l_C
		if l_A + l_B == l_C or l_A == l_B + l_C or l_A + l_C == l_B:
			# print A, B
			c += 1
print n, c, len(coords)