#!/usr/bin/env python

from Functions import fac
x = int(raw_input('Grootte raster in x- en y-richting: '))
combi = fac(2*x)/fac(x)**2
print combi