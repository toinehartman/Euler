#!/usr/bin/env python

from Functions import primegen
from string import digits
from itertools import permutations

p = primegen(18)
nums = permutations(digits)
summ = 0

for perm in nums:
	if not perm[0] == "0":
		# print perm
		c = 0
		ok = False
		for i in xrange(1, 8):
			n = ""
			for j in xrange(i, i+3):
				n = "{0}{1}".format(n, perm[j])
			# print n
			n = int(n)
			if  not n % (p[c]):
				ok = True
			else:
				ok = False
				break
			c += 1
		if ok:
			t = ""
			for a in perm:
				t = "{0}{1}".format(t, a)
			summ += int(t)
			print perm
			# raw_input('#.. ')
print summ