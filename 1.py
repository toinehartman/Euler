#!/usr/bin/env python

# summ = 0
# for i in xrange(334):
# 	summ += i * 3
# 	if (i * 5)%3 != 0 and i * 5 < 1000:
# 		summ += i * 5
# print 'Total sum: {0}'.format(summ)

print 'Total sum:', sum(filter(lambda x: not (x % 3 and x % 5), range(1000)))

print 'Total sum:', sum(x for x in range(1000) if not (x % 3 and x % 5))
