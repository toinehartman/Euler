#!/usr/bin/env python

must = ["the", "one", "in", "he", "to", "of", "and"]

for a in xrange(97, 123):
	for b in xrange(97, 123):
		for c in xrange(97, 123):
			s = ""
			n = -1
			cipher = open("cipher1.txt", "r")
			for line in cipher:
				l = line.replace("\n", "").split(",")
				for char in l:
					char = int(char)
					n += 1
					if n%3 == 0:
						m = char^a
					elif n%3 == 1:
						m = char^b
					elif n%3 == 2:
						m = char^c
					if m >= 32 or m == 10:
						s += chr(m)
			if all(w in s for w in must):
				print "Password: '{0}{1}{2}' (som: {4}):\n{3}\n".format(chr(a), chr(b), chr(c), s[:50], sum(ord(x) for x in s))
				print s, "\n"
			cipher.close()
