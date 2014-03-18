#!/usr/bin/env python

m = [0, 0]
i = 0
with open('base_exp.txt') as f:
	for line in f:
		i += 1
		a = int(line.split(',')[0])
		b = int(line.split(',')[1])
		p = a**b
		if p > m[1]:
			m = [i, p]
			print i