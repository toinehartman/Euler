#!/usr/bin/env python

from string import ascii_uppercase

f = open('names.txt', 'r')
s = str(f.readlines())
f.close()
n = s.replace('"','').replace("'","").replace(']','').replace('[','').split(',')
n.sort()
summ = 0
count = 0
# len(n) = 5163
alpha = ascii_uppercase #['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in xrange(0, len(n)):
	nscore = 0
	letters = list(n[i])
	count += 1
	# print i+1, n[i],
	for l in letters:
		# print alpha.index(l)+1,
		nscore += alpha.index(l)+1
		# print nscore,
	summ += nscore * (i + 1)
	# print ''
print summ, count
