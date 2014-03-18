#!/usr/bin/env python

# KUTMETHODE

# num = 10
# c = 0

# while 1:
# 	for a in xrange(10):
# 		if sum(map(int, list(str(num))))**a == num:
# 			c += 1
# 			print c, num
# 			break
# 	num += 1


# CHILLE METHODE

base = 4
l = []
print 'Lijst van machten maken'
while base < 10**5:
	for a in xrange(2, 10):
		l.append([base**a, base])
	base += 1
print 'Lijst van machten sorteren'
l.sort()

print 'Zoeken naar matches'

c = 0
for p in l:
	if sum(map(int, list(str(p[0])))) == p[1]:
		c += 1
		print c, p
