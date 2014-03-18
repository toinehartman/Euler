#!/usr/bin/env python

from itertools import permutations
from time import *

matrix = []

print 'Bestand laden'
for line in open('matrix.txt', 'r'):
	matrix.append(line.replace('\n', '').split(','))
	# print line.split(',')

# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37, 331]]

print 'Grootte matrix bepalen'
dim = len(matrix)

print 'Alle permutaties proberen'
min_total = 0
for s in set(p for p in permutations([1 for x in xrange(dim - 1)] + [0 for y in xrange(dim - 1)])):
	i, j = 0, 0
	total = int(matrix[i][j])

	for step in s:
		if step == 1:
			i += 1
		elif step == 0:
			j += 1
		total += int(matrix[i][j])
	if total < min_total or min_total == 0:
		min_total = total
	print total
print 'Klaar!', min_total