#!/usr/bin/env python

from Functions import *
from time import time

tic = time()

ratio = 0
num = 0
b = 0
while ratio < 0.99:
	num += 1
	b += bouncy(num)
	ratio = float(b) / num
print ratio, b, num, time() - tic

tic = time()

ratio = 0
num = 0
b = 0
while ratio < 0.99:
	num += 1
	b += alt_bouncy(num)
	ratio = float(b) / num
print ratio, b, num, time() - tic
