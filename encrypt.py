#!/usr/bin/env python

# ENCRYPT USING XOR

from sys import argv
from time import time
from Functions import *
from os import path
from os import rename

iname = raw_input('\nFile to encrypt:\t')
key = raw_input('Encyption key:\t\t')

newname = path.splitext(iname)[0] + '_backup' + path.splitext(iname)[1]
rename(iname, newname)

ifile = open(newname, 'r')
encr = encrypt(ifile.read(), key)
ifile.close()

print '\nEncrypted..!\n'

ofile = open(iname, 'w')
ofile.writelines(encr)
ofile.close()

print 'Encrypted file: "{0}"\n'.format(iname)