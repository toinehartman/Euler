#!/usr/bin/env python

summ = 0
for n in xrange(1,1001):
	summ += n**n
print str(summ)[-10:]

print str(sum(n**n for n in xrange(1, 1001)))[-10:]