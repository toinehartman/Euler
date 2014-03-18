#!/usr/bin/env python

from Functions import fibo
import string
from time import time
tic = time()
ttic = tic
count = -1
d = set(string.digits[1:])
for f in fibo():
	count += 1
	if not count%10000:
		print count, len(str(f)), time()-tic
		tic = time()
	if set(str(f)[-9:]) == d == set(str(f)[:9]):
		print "{0}, {1} minuten, {2}, {3}".format(count, ttic, str(f)[:9], str(f)[-9:])
		break
