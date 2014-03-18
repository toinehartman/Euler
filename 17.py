#!/usr/bin/env python

from num2words import base, lang_EN

lim = 1000
l = 0
for num in xrange(1, lim+1):
	numForm = lang_EN.to_card(num).replace(' ','').replace('-','').replace(',','')
	l += len(repr(numForm).replace("'", "")[1:])
	print repr(numForm).replace("'", "")[1:]
print l