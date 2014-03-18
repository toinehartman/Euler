#!/usr/bin/env python

f_1 = 0
s_1 = 0
for n in xrange(10**9):
	f_1 += str(n).count('1')
	if f_1 == n:
		s_1 += f_1
		print n, s_1