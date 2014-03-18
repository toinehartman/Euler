#!/usr/bin/env python

from Functions import isPalindrome
summ = 0
for n in xrange(1000001):
	if isPalindrome(n) and isPalindrome(str(bin(n))[2:]):
		print '{0}: {1}'.format(n, bin(n))
		summ += n
print 'Som: {0}'.format(summ)

print 'Som: {0}'.format(sum(n for n in xrange(1000001) if isPalindrome(n) and isPalindrome(str(bin(n))[2:])))