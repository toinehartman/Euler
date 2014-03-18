#!/usr/bin/env python

import time
from Functions import fac
end = 7*fac(9)+1
numsum = 0
for n in xrange(1, end):
	facsum = 0
	if len(str(n)) > 1:
		for i in list(str(n)):
			facsum += fac(int(i))
		if facsum == n:
			print n
			numsum += n
print '------'
print numsum