#!/usr/bin/env python

from itertools import permutations
nums = '0123456789'
print nums
perms = [x for x in permutations(nums)]
print 'Miljoenste permutatie:',str(perms[10**6-1]).replace("'","").replace(',','').replace('(','').replace(')','').replace(' ','')