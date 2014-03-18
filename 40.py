#!/usr/bin/env python

d = '0'
n = 1
while len(d) < 10**6+1:
	d += str(n)
	n += 1
print int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000])
print d[1], d[10], d[100], d[1000], d[10000], d[100000], d[1000000]
