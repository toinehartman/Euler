#!/usr/bin/env python

from itertools import permutations
import string

def c_lex(s):
	l = 0
	for i in xrange(1, len(s)):
		if ord(s[i]) > ord(s[i - 1]):
			l += 1
			# print s[i], s[i-1]
	return l

# for w in ['abc', 'hat', 'zyx']:
# 	print c_lex(w)

p_max = 0
for n in xrange(27):
	p = 0
	perms = [x for x in permutations(string.lowercase, n)]
	for w in perms:
		if c_lex(w) == 1:
			p += 1
	# print p
	if p > p_max:
		print 'n: {0}, p: {1}, verhouding kloppend:{2}'.format(n, p, p/float(len(perms)))
		p_max = p