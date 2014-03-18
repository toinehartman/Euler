#!/usr/bin/env python

def trigen(l):
	from time import time
	from random import randint

	lines = list()
	rowstr = str()
	tic = time()
	for i in xrange(0,l+1):
		row = list()
		for j in xrange(0,i):
			row.append(str(randint(0, 99)).zfill(2))
			rowstr = ' '.join(map(str, row))
		lines.append(rowstr)
		lines = filter(None, lines)
		linesstr = '\n'.join(map(str, lines))

	f = open('trigen%d.txt' % l, 'w')

	f.writelines( linesstr )

	return time()-tic