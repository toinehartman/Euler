#!/usr/bin/env python

from Functions import isPrime
from itertools import permutations

a = []
for n in xrange(1000, 10000):
	perms = sorted(set(permutations(str(n))))
	nums = []
	# print perms
	for p in perms:
		# print p
		n = ""
		for char in str(p):
			if char.isdigit():
				n += char
		nums.append(int(n))
	# print nums
	for i in xrange(0, len(nums)-2):
		for j in xrange(i+1, len(nums)-1):
			for k in xrange(j+1, len(nums)):
				if nums[k]-nums[j] == nums[j]-nums[i] and isPrime(nums[i]) and isPrime(nums[j]) and isPrime(nums[k]) and not nums[i] in a and len(str(nums[i])) == 4:
					print "{0}{1}{2}".format(nums[i], nums[j], nums[k])
					a.append(nums[i])