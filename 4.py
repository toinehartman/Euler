#!/usr/bin/env python

from Functions import isPalindrome
largest = 0
n = 100
while n < 1000:
	for i in xrange(100,1000):
		result = i * n
		if isPalindrome(result) == True:
			if result > largest:
				largest = result
				print largest,
	n += 1
# 		print i
# while 1:
#  	n = raw_input('>> ');
#  	print str(isPalindrome(n));