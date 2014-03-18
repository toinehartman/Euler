#!/usr/bin/env python

c = 0
for n in xrange(1, 10**7):
	if str(n)[-1] != '0' and any(d in ['1', '3', '5', '7', '9'] for d in '146') and all(int(d) % 2 for d in str(n + int(str(n)[::-1]))):
		c += 1
print c