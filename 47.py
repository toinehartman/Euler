#!/usr/bin/env python

from Functions import isPrime
from Functions import pfactors

n1 = 0

while 1:
	divs = pfactors(n1)
	n1 += n1
	if all(isPrime(d) for d in divs) and divs != [] and len(set(divs)) == 4:
		n2 = n1 + 1
		divs = pfactors(n2)
		if all(isPrime(d) for d in divs) and divs != [] and len(set(divs)) == 4:
			n3 = n2 + 1
			divs = pfactors(n3)
			if all(isPrime(d) for d in divs) and divs != [] and len(set(divs)) == 4:
				n4 = n3 + 1
				divs = pfactors(n4)
				if all(isPrime(d) for d in divs) and divs != [] and len(set(divs)) == 4:
					print n1, n2, n3, n4
					break