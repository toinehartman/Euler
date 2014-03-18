#!/usr/bin/env python

dim = 1001
d = []
num = 1
for i in xrange(1, (dim-1)/2+1):
	for x in xrange(1, 5):
		d.append(num)
		num += i * 2
d.append(dim**2)
# print d
print sum(d)