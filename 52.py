#!/usr/bin/env python

print set(str(65734))
n = 1
while 1:
	twee = 2*n
	drie = 3*n
	vier = 4*n
	vijf = 5*n
	zes = 6*n
	if set(str(n)) == set(str(twee)) == set(str(drie)) == set(str(vier)) == set(str(vijf)) == set(str(zes)):
		print n
		break
	n += 1