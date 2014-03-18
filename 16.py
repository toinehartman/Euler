#!/usr/bin/env python

num = str(2**1000)
summ = 0
for i in num:
	summ += int(i)
print summ

print sum(int(c) for c in str(2**1000))