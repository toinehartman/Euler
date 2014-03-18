#!/usr/bin/env python

import string

old = 0
new = 0
ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
nums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
delete_table = string.maketrans(string.ascii_uppercase, ' ' * len(string.ascii_uppercase))

with open('roman.txt', 'r') as roman:
	for line in roman:
		n = 0
		l = line.translate(None, delete_table)
		old += len(l)

		for i in xrange(len(l)):
			c = l[i]
			value = ints[nums.index(c)]
			try:
				# als volgende letter groter is wordt de huidige negatief
				nextValue = ints[nums.index(l[i + 1])]
				if nextValue > value:
					value *= -1
			except IndexError:
				# geen volgende letter
				pass
			n += value

		r = ''
		for i in range(len(ints)):
			count = int(n/ints[i])
			r += nums[i] * count
			n -= ints[i] * count
		new += len(r)
		print l, n, r
print old, new, 'difference:', old - new