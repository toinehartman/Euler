#!/usr/bin/env python

from Functions import *

m = 0
for a in xrange(10**10):
	if len(set(pfactors(a))) > m:
		m = len(set(pfactors(a)))
		print m, a