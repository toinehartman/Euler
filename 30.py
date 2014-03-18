#!/usr/bin/env python

sum5 = 0
lim = input('Limiet: ')
for i in xrange(2,lim):
	for p in xrange(3,int(len(str(lim))+1)):
		summ = 0
		for n in xrange(1,len(str(i)) + 1):
			summ += int(str(i)[n-1:n])**p
		if summ == i:
			print p,':',i
			if p == 5:
				sum5 += i
print sum5