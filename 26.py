#!/usr/bin/env python

max_l = [0, 0]

for d in xrange(2, 1000):
	frac = '0.'
	den = d
	cond = []
	enum = 10
	r = 0
	while len(frac) < 10000:
		if enum == 0 or den == 0:
			# print 'den 0', frac
			break
		while enum // den == 0:
			enum *= 10
			frac += '0'
			# print 'intdeling 0', frac
		if not [enum // den, enum % den] in cond:
			frac += str(enum // den)
			cond.append([enum // den, enum % den])
			enum = 10 * (enum % den)
		else:
			r = len(cond) - cond.index([enum // den, enum % den])
			break

	if r > max_l[1]:
		max_l = [d, r]
	if r != 0: print '1/{0} = {1}, {2}'.format(d, frac, r)
print max_l