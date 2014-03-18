#!/usr/bin/env python

from Functions import penta
p = []
l = 10000
Dl = 10**10
for i in xrange(1, l):
	p.append(penta(i))
print "List created"
for a in p:
	for b in p:
		S = a + b
		D = abs(a - b)
		if S in p and D in p and D < Dl:
			print "Verschil: {0}".format(D)
			Dl = D
print Dl