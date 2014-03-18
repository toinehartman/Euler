#!/usr/bin/env python

from math import *
from time import *

r = 0
while (1):
	print ' ' * int(ceil(50 * (sin(r) + 1))) + 'sss'
	r = r + 0.05
	sleep(10**-2)
