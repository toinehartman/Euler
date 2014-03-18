#!/usr/bin/env python

import os

d = '/Users/Toine/Development/Euler/'

for file in os.listdir(d):
	fname = str(file)
	if fname[-3:] == '.py':
		# print fname
		f = open(d + fname, 'rw')
		contents = f.readlines()
		if '#!/usr/bin/env python\n' in contents: continue
		open(d + fname, 'w').writelines(['#!/usr/bin/env python\n', '\n'] + contents)
		os.system('chmod +x ' + d + fname)
print 'Euler-files updated!'
