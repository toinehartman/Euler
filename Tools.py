#!/usr/bin/env python

#Bestaat uit:
#
#Priemgetalchecker
#permutaties maker
#combinaties maker
#coprime checker
#priemgetal generator
#permutatie checker
#
#4 jan 2012
#
#Gebruik: 
#import Tools
#Tools.isprime(3)
#
#of: 
#from Tools import isprime
#isprime(3)
#

from math import sqrt, factorial

def getlines(path):
	with open(path, 'r') as f:
		for line in f:
			yield line.strip()
		f.close()

def factors(num):
	if num<1 or num%1: return []
	factors = []
	for x in primegen(num):
		while not num%x:
			factors.append(x)
			num/=x
		if isprime(num):
			factors.append(num)
			return factors
		elif num == 1:
			return factors


#PRIEMGETALCHECKER
#Geeft True voor een priemgetal, anders een False
#input moet een integer zijn
def isprime(x):
	if x == 2 or x == 3: return True	
	# elif x == 1 or not x % 2 or x%1: return False
	elif x == 1 or not ((not (x-1) % 6) or (not (x+1) % 6)): return False
	c = int(sqrt(x))+1
	for y in xrange(5,c,6):
		if not x % y or not x%(y+2):
			return False
	return True


#prime number generator
#produceert alle priemgetallen net als xrange alle positieve gehele getallen produceert.
#gebruik: for x in Tools.primenums():

def primegen(Max = 0):
	#elk priemgetal > 3 is van de vorm 6n +/-1 dus alleen die getallen hoeven te worden gecheckt.
	n = 5
	yield 2
	yield 3
	while not Max or n < Max:
		if isprime(n+2):
			yield n+2
		if isprime(n):
			yield n
		n += 6
