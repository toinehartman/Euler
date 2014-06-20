#!/usr/bin/env python
from Functions import *

primes = [3, 3, 3, 3]
for i in primesix(1000):
	for j in primesix(1000):
		for k in primesix(1000):
			for l in primesix(1000):
				if isPrime(int(str(i) + str(j))) and isPrime(int(str(j) + str(i))) and isPrime(int(str(i) + str(k))) and isPrime(int(str(k) + str(i))) and isPrime(int(str(i) + str(l))) and isPrime(int(str(l) + str(i))) and isPrime(int(str(j) + str(k))) and isPrime(int(str(k) + str(j))) and isPrime(int(str(j) + str(l))) and isPrime(int(str(l) + str(j))) and isPrime(int(str(k) + str(l))) and isPrime(int(str(l) + str(k))):
					print i, j, k, l