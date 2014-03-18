#!/usr/bin/env python

from Functions import Divisors
from time import time
integers = xrange(1,28124)
abu = []
sumOfAbu = []
tic = time()
for i in integers:
	if sum(Divisors(i)) > i:
		abu.append(i)
# print abu
print 'Abu: {0} s'.format(round(time() - tic, 3))

for i in abu:
	for n in abu:
		sumOfAbu.append(i + n)
print 'Sum of abu: {0} s'.format(round(time() - tic, 3))

sua = set(sumOfAbu)
ints = set(integers)

print 'Som van alle niet-abu-sommen: {0}'.format(sum(ints - sua))

# for i in ints:
# 	for n in abu:
# 		if i > n and i - n in abu:
# 			# print '{0} is som van twee "abundant numbers".'.format(i)
# 			sumOfAbu.append(i)
# 			break
# 	# if not i%1000:
# 		# print i
# 	# print 'Volgende abu: {0}'.format(time() - tic)
# print sumOfAbu
print 'Eind: {0} s'.format(round(time() - tic, 3))
# print Functions.Divisors(input('...'))