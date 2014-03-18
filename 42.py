#!/usr/bin/env python

from string import ascii_uppercase

alpha = list(ascii_uppercase)
triangle = []
count = 0

for i in xrange(101):
	triangle.append(int(0.5*i*(i+1)))
f = open('words.txt', 'r')
for line in f:
	w = line
words = w.replace('"', '').split(',')
for word in words:
	wordsum = 0
	letters = list(word)
	for l in letters:
		wordsum += alpha.index(l)+1
	if wordsum in triangle:
		print wordsum,
		count += 1
print ''
print count