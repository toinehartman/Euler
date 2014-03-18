#!/usr/bin/env python

import time
pan = ""
for a in xrange(1, 9876543210):
	for c in xrange(1, 9876543210):
		b = int(c/a)
		# print a,b,c
		# print b
		# time.sleep(0.01)
		pan = str(a) + str(b) + str(c)
		# pand = True
		if len(pan) == 10:
			print a, b, c, pan