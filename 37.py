#!/usr/bin/env python

from Functions import isPrime
found = 0
summ = 0
num = 11
while found < 11:
	results = []
	for i in xrange(len(str(num))-1, -1, -1):
		# print str(num)[i:]
		# print str(num)[:i+1]
		if isPrime(int(str(num)[i:])) and isPrime(int(str(num)[:i+1])):
			results.append('1')
		else:
			results.append('0')
			break
	# print results
	if not '0' in results:
		found += 1
		summ += num
		print '{0} is het {1}e getal waarvoor dit geldt.'.format(num, found)
	num += 2
	# raw_input('...')
print 'Som: {0}'.format(summ)