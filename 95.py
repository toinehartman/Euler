#!/usr/bin/env python

from Functions import *

l_chain = []
for n in xrange(12496, 10**6 + 1):
	c = n
	i = 0
	chain = []
	while c not in chain and len(chain) < 50:
		i += 1
		chain.append(c)
		# print c
		c = sum(Divisors(c))
	if c == n and all(num <= 10**6 for num in chain):
		if len(chain) > len(l_chain):
			l_chain = chain
			print n, len(chain), min(chain)
		else:
			print n, 'chain'
	elif not n % 50: print n