#!/usr/bin/env python

from def_timetest_trigen import trigen
import xlwt
book = xlwt.Workbook()
sheet1 = book.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Correlatie')
s = int(raw_input('Begin?...          '))
e = int(raw_input('Eind?...           '))
st = int(raw_input('Stapgrootte?...   '))

n = 1
for lijn in xrange(s,e,st):
	tijd = round(float(trigen(lijn)),4)
	print '{0}: {1:.4f} s'.format(lijn, tijd)
	sheet1.write(n, 0, lijn)
	sheet1.write(n, 1, tijd)
	sheet1.write(n, 2, tijd**0.5)
	n += 1
book.save('trigen_corr.xls')