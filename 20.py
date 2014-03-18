#!/usr/bin/env python

from Functions import fac

Faculteit = fac(input('Getal? : '))
print 'Faculteit is', Faculteit
# list(str(Faculteit))
print sum(map(int,str(Faculteit)))