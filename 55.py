#!/usr/bin/env python

from Functions import isPalindrome

count = 0
for n in xrange(1, 10000):
	i = 0
	num = n
	Lychrel = True
	while Lychrel == True and i < 50:
		i += 1
		num += int(str(num)[::-1])
		if isPalindrome(num):
			Lychrel = False
			break
		elif not isPalindrome(num) and i == 49:
			count += 1
			print count, n
print "Aantal Lychrel-getallen onder 10000: {0}".format(count)