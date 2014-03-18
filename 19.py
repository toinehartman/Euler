#!/usr/bin/env python

# 1 jan 1900 is een maandag
# 1 jan 1901 is een dinsdag
# 2 dagen eerder en elke 7 dagen later zijn dus zondagen

d = 6
m = 1
y = 1901

count = 0

long = [1, 3, 5, 7, 8, 10, 12]
short = [4, 6, 9, 11]
leap = [2]

while y < 2001:
	d += 7

	if m in leap:
		if not y%400:
			if d > 29:
				m += 1
				d -= 29
		elif not y%4:
			if d > 29:
				m += 1
				d -= 29
		else:
			if d > 28:
				m += 1
				d -= 28
	elif m in short and d > 30:
		m += 1
		d -= 30
	elif m in long and d > 31:
		m += 1
		d -= 31
	
	if m > 12:
		y += 1
		m -= 12

	if d == 1:
		count += 1
		print '{3}: {0:0d}-{1:0d}-{2:0d}'.format(d, m, y, count)