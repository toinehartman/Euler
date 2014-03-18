#!/usr/bin/env python

coins = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200
ways = [None] * (target + 1)
ways[0] = 1

for i in xrange(len(coins)):
	for j in xrange(coins[i], target + 1):
		if ways[j] == None:
			ways[j] = ways[j - coins[i]]
		else:
			ways[j] += ways[j - coins[i]]
print ways[len(ways) - 1]

count = 0
for a in xrange(200/coins[0]+1):
	for b in xrange(200/coins[1]+1):
		for c in xrange(200/coins[2]+1):
			for d in xrange(200/coins[3]+1):
				for e in xrange(200/coins[4]+1):
					for f in xrange(200/coins[5]+1):
						for g in xrange(200/coins[6]+1):
							for h in xrange(200/coins[7]+1):
								if a*coins[0]+b*coins[1]+c*coins[2]+d*coins[3]+e*coins[4]+f*coins[5]+g*coins[6]+h*coins[7] == 200:
									# print "{0} x {1}p + {2} x {3}p + {4} x {5}p + {6} x {7}p + {8} x {9}p + {10} x {11}p + {12} x {13}p + {14} x {15}p = 200p".format(a,coins[0],b,coins[1],c,coins[2],d,coins[3],e,coins[4],f,coins[5],g,coins[6],h,coins[7])
									count += 1
print count