#!/usr/bin/env python

from time import time
from Functions import *
tic = time()
print 'Aantal: {0}, {1:.02f} s dmv sum en all()'.format(sum(1 for p in prigen(10**6) if all(isPrime(x) for x in rotations(p))), time()-tic)