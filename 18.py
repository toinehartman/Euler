#!/usr/bin/env python

from time import time
lines = list()
fileName = raw_input('Driehoeksbestand?...:   ')
tic = time()
if fileName == '':
	fileName = 'triangle18.txt'
tri = open(fileName, 'r')
l = len(open(fileName).readlines(  ))
print 'Lengte: {0}'.format(l)
for line in tri:
	line = line.replace('\n', '')
	nums = line.split(' ')
	lines.append(nums)
tri.close()

for i in xrange(l-1,0,-1):
	for n in xrange(0,i):
		if int(str(lines[i][n]).strip(' ')) > int(str(lines[i][n+1]).strip(' ')):
			lines[i-1][n] = int(str(lines[i-1][n]).strip(' ')) + int(str(lines[i][n]).strip(' '))
		else:
			lines[i-1][n] = int(str(lines[i-1][n]).strip(' ')) + int(str(lines[i][n+1]).strip(' '))
print 'Grootste som: {0}'.format(lines[0][0])

print 'Tijd: {0:.2f} s'.format(time()-tic)