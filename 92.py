#!/usr/bin/env python

c = 0
for n in xrange(1, 10**7):
	a = n
	while a != 1 and a != 89:
		a = sum(int(i)**2 for i in str(a))
		# print a,
	if a == 89:
		c +=1
	if not n%10**5:
		print n
print c