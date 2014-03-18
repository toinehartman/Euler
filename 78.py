#!/usr/bin/env python

n = 1
p = []
p.append(1)
while 1:
	i = 0
	penta = 1
	p.append(0)

	while penta <= n:
		if i % 4 > 1:
			sign = -1
		else:
			sign = 1
		p[n] += sign * p[n - penta]
		p[n] %= 10**6
		i += 1

		if not i % 2:
			j = i // 2 + 1
		else:
			j = -(i // 2 + 1)
		penta = j * (3 * j - 1) / 2
		
	if not p[n]: break
	n += 1
print n