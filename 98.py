#!/usr/bin/env python

from string import digits
from itertools import permutations
import sys
import time

tic = time.time()
count = 0
w_count = 0
f = open('words.txt', 'r')
for line in f:
	w = line
words = w.replace('"', '').split(',')

skip = []
c = []
d = []
for a in words:
		for b in words[words.index(a):]:
			if not [a, b] in skip:
				if words.index(a) != words.index(b) and set(a) == set(b) and len(a) == len(b):
					skip.append([b, a])
					c.append([a, b])
					d.append(a)
					print a, b
print len(words), len(d), round(time.time()-tic, 4), 's'

dig = digits[::-1]
for word in d:
	print len(word), word
	for i in xrange(0, len(set(word))):
		for j in dig[:len(set(word))]:
			print word.replace(list(set(word))[i], j)
	print ''