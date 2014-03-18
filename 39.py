#!/usr/bin/env python

maxi = [0, 0]
max = 1000
for p in xrange(max+1):
	rects = []
	for a in xrange(1, p+1):
		for b in xrange(1, p+1):
			rect = []
			c = (a**2 + b**2)**0.5
			if int(c)**2 == a**2 + b**2 and a+b+c == p:
				c = int(c)
				rect = sorted([a, b, c])
				if not rect in rects:
					rects.append(rect)
	if len(rects) > 0:
		print p, rects
	if len(rects) > maxi[1]:
		maxi[0] = p
		maxi[1] = len(rects)
print 'Meeste oplossingen voor p = {0}, namelijk {1}'.format(maxi[0], maxi[1])