#!/usr/bin/env python

from Functions import isPrime

con = 0
for a in xrange(-1000, 1000):
	for b in xrange(-1000, 1000):
		conpri = True
		n = -1
		while conpri:
			n += 1
			pospri = n**2 + a*n + b
			conpri = isPrime(pospri)
		if n > con:
			con = n
			prod = a*b
			print con, prod
print '{0} primes voor a*b={1}'.format(con, prod)