#!/usr/bin/env python

from math import sqrt
from itertools import cycle
from time import time
import os
from shutil import copyfile
from string import digits

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def encrypt(in_path, key = 'loremipsum', enc_hex = True, log = True):
	tic = time()
	l = len(key)
	print '\n- encrypt mode' 

	backupname = os.path.splitext(in_path)[0] + '.backup' + os.path.splitext(in_path)[1]
	copyfile(in_path, backupname)
	outfile = open(in_path, 'w')
	infile = open(backupname, 'r')

	if enc_hex:
		for key_c in cycle(key):
			c = infile.read(1)
			if not c:
				break
			outfile.write('0x' + str((hex(ord(c) ^ ord(key_c))[2:]).zfill(2)))
	else:
		for key_c in cycle(key):
			c = infile.read(1)
			if not c:
				break
			outfile.write((ord(c) ^ ord(key_c)).zfill(3))
	outfile.close()

	print "\nEncrypted with key: '{0}'\n".format(key)
	print "{0} s".format(round(time()-tic, 4))

def decrypt(in_path, key, log = True):
	tic = time()
	l = len(key)
	print '\n- decrypt mode'

	backupname = os.path.splitext(in_path)[0] + '.hex' + os.path.splitext(in_path)[1]
	copyfile(in_path, backupname)
	outfile = open(in_path, 'w')
	infile = open(backupname, 'r')

	if all(c in digits + 'abcdefx' for c in infile.read()):
		print "\nHEXADECIMAL"
		for key_c in cycle(key):
			c = infile.read(4)
			if not c:
				break
			print key_c, c
			outfile.write(chr(int(c, 16) ^ ord(key_c)))
	else:
		print "\nDECIMAL"
		for key_c in cycle(key):
			c = infile.read(3)
			if not c:
				break
			outfile.write(chr(int(c, 10) ^ ord(key_c)))
	outfile.close()

	print "\nDecripted with key '{0}'\n".format(key)
	print "{0} s".format(round(time()-tic, 4))

def isDivisible(enum, denom):
	'''Check wether enum is divisible by denom.'''

	return not enum%denom
	
def isEven(num):
	'''Check wether num is even.'''

	return not num%2

def isPalindrome(string):
	'''Check if string is a palindrome.'''

	return str(string) == str(string)[::-1]

def isPrime(num):
	'''Check is num is prime.

	It uses the fact that every prime (except 2 and 3) is k * 6 +- 1.'''

	if num == 2 or num == 3: return True
	elif num == 1 or not ((not (num - 1) % 6) or (not (num + 1) % 6)): return False
	l = int(sqrt(num)) + 1
	for d in xrange(5, l, 6):
		if not num % d or not num % (d + 2):
			return False
	return True

def sieve_list(limit):
	'''Sieve a list of primes including the number limit (if prime).'''

	s = [2] + range(3, limit + 1, 2)
	i = 0
	while i < len(s):
		for n in s:
			if not n % s[i] and n != s[i]:
				del(s[s.index(n)])
		i += 1
	return s

def primegen(limit):
	'''Create a list of primes including the number limit (if prime).'''

	primes = []
	for i in xrange(1, limit+1):
		if isPrime(i):
			primes.append(i)
	return primes

def prigen(limit = 0):
	'''Generate primes up to limit if specified, or infinitely if not.'''

	yield 2
	if not limit:
		s = 3
		while 1:
			if isPrime(s):
				yield s
				s += 2
	for n in xrange(3, limit + 1, 2):
		if isPrime(n): yield n

def primesix(limit = 0):
	'''Generate primes up to limit if specified, or infinitely if not.'''

	yield 2
	yield 3

	k = 1
	p = k * 6 - 1
	while p <= limit:
		if isPrime(p) and p < limit: yield p
		p = k * 6 + 1
		if isPrime(p) and p < limit: yield p
		k += 1
		p = k * 6 - 1

def fac(num):
	'''Return factorial of num.'''

	f = 1
	for i in xrange(1, num+1):
		f *= i
	return f

def Divisors(num):
	'''Return list of divisors of num.'''

	divs = []
	for i in xrange(1, int(num**0.5)+1):
		if isDivisible(num, i):
			divs.append(i)
			if num/i != num and num/i != i:
				divs.append(num / i)
	divs.sort()
	return divs

def fibo(lim = 0):
	'''Generate Fibonacci numbers up to limit if specified, or inifnitely if not.'''

	a, b = 0, 1
	yield a
	yield b
	while lim == 0 or b <= lim:
		a, b = b, a + b
		yield b

def penta(num):
	n = num+1
	return n*(3*n-1)/2

def invpenta(p):
	p = float(p)
	return sqrt((p*2+p)/3)

def pfactors(num, unique = False):
	'''Return list of primefactors of num.

	unique = False leaves mulitple primefactors intact, unique = True filters them (distinct).'''

	finished = False
	f = []
	if isPrime(num): return [num]
	for d in xrange(2, int(sqrt(num)) + 1):
		if not finished:
			while 1:
				if isPrime(num):
					f.append(num)
					finished = True
					break
				elif not num % d and isPrime(d):
					num /= d
					f.append(d)
				else:
					break
		else:
			break
	if unique: return list(set(f))
	return f

def rad(n):
	'''Returns product of unique primefactors of n.'''

	p = 1
	for a in pfactors(n, True):
		p *= a
	return p

def isPandigital(num, lower_lim = 1, upper_lim = 9):
	'''Returns True if all number from lower_lim to upper_lim are present once in num.'''

	digits = [int(x) for x in str(num)]
	if all(d <= upper_lim for d in digits) and all(d >= lower_lim for d in digits):
		if len(set(digits)) == len(digits):
			return True

def combicount(total, count):
	'''Returns number of possible combinations.'''

	return fac(total)/(fac(count)*fac(total-count))

def rotations(num):
	'''Returns all rotations of input.'''

	if type(num) is int:
		dig = list(str(num))
		l = len(str(num))
	elif type(num) is str:
		dig = list(num)
		l = len(num)
	elif type(num) is list:
		l = len(num)
		if type(num[0]) is str:
			dig = map(int, dig)
		else:
			try:
				dig = num
			except:
				sys.exit('\nERROR\n')
	else:
		l = len(num)
		dig = list(num)
		
	n = [None]*l
	for i in xrange(0, l):
		t = dig[i]
		for j in xrange(l-1, 0, -1):
			n[j] = dig[(j+i)%l]
		n[0] = t
		n = map(str, n)
		yield int("".join(n))

def gcd(p, q):
	'''Returns gcd of p and q.'''

	while p % q:
		p, q = q, p % q
	return q

def rec_gcd(p, q):
	'''Returns gcd of p and q (recursively).'''

	if q == 0: return p
	return rec_gcd(q, p % q)

def euc_gcd(a, b):
	'''Returns gcd of a and b (by Euclides' method).'''

	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
	return a

def bit_gcd(u, v):
	'''Returns gcd of u and v (by bitwise operations).'''

	if u == v: return u
	if u == 0: return v
	if v == 0: return u
	if ~u & 1:
		if v & 1:
			return bit_gcd(u >> 1, v)
		else:
			return gcd(u >> 1, v >> 1) << 1
	if ~v & 1: return gcd(u, v >> 1)
	if u > v: return gcd((u - v) >> 1, v)
	return gcd((v - u) >> 1, u)

def pyramidal(n_lim):
	n = 1
	while n < n_lim:
		yield (2 * n**3 + 3 * n**2 + n)/6
		n += 1

def bouncy(num):
	'''Returns True if num is not increasing and not decreasing.'''

	num = str(num)
	decr = False
	incr = False
	for i in xrange(1, len(num)):
		if int(num[i]) > int(num[i - 1]):
			if decr: return True
			incr = True
		if int(num[i]) < int(num[i - 1]):
			if incr: return True
			decr = True
	return decr and incr

def alt_bouncy(num):
	s = ''.join(sorted(str(num)))
	return str(num) != s and str(num) != s[::-1]

def abc_hit(a, b, c):
	'''Returns True is the triplet (a, b, c) is an abd-hit.'''
	
	if a < b and gcd(a, b) == 1 and gcd(a, c) == 1 and a + b == c and gcd(b, c) == 1 and len(set(pfactors(a*b*c))) < c:
		return True
	return False

def time_step(reset = False):
	if reset:
		yield time_step(False)
	else:
		t = time()
		while 1:
			t = time() - t
			yield t
