'''Read an integer N.

Without using any string methods, try to print the following: 
"123...N"


Note that "..." represents the values in between.
'''
from __future__ import print_function
print(*range(1, int(input())+1), sep='')
