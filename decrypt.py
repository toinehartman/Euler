#!/usr/bin/env python

# DECRYPT USING XOR

from sys import argv
from time import time
from Functions import *
from os import system
from os import path
from os import rename

iname = raw_input('\nFile to decrypt:\t')
key = raw_input('Encryption key:\t\t')

newname = path.splitext(iname)[0] + '_enc_backup' + path.splitext(iname)[1]
rename(iname, newname)

ifile = open(newname, 'r')
decr = decrypt(ifile.read(), key)
ifile.close()

print '\nDecrypted..!\n'

ofile = open(iname, 'w')
ofile.writelines(decr)
ofile.close()

print 'Decrypted file: "{0}"\n'.format(iname)
system('open {0}'.format(iname))