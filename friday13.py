#!/usr/bin/env python

# -*- coding: utf-8 -*-

from sys import argv

d = 4
m = 1
y = 2013

low_lim = 2013
count = 0
max_f = 0
one = False

long = [1, 3, 5, 7, 8, 10, 12]
short = [4, 6, 9, 11]
leap = [2]

def print_fridays(year, fridays):
	days = {1:'één', 2:'twee', 3:'drie'}
	if fridays != 1:
		print "{0} heeft {1} vrijdagen de 13e".format(year, days[fridays])
	else:
		print "{0} heeft {1} vrijdag de 13e".format(year, days[fridays])

if len(argv) == 2:
	lim = int(argv[1])
	one = True
elif len(argv) == 3:
	low_lim = int(argv[1])
	lim = int(argv[2])
else:
	lim = 2020

while y <= lim:
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
		if not one and y >= low_lim:
			print_fridays(y, count)
		elif y == lim:
			print_fridays(y, count)
		count = 0
		y += 1
		m -= 12

	if d == 13:
		count += 1
		if count > max_f:
			max_f = count
		# print '{3}: {0:0d}-{1:0d}-{2:0d}'.format(d, m, y, count)