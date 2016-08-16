#!/bin/python

# primefinder.py <length of prime>

import sys

digits=int(sys.argv[1])

f = open('e10000')
file = f.read()


def isprime(a):
    if a % 2 != 0:
        return all(a % i for i in range(3,a,2))


def collector(a):
    for i in range(151,201):
        out = ''
        for x in range(i,i+a):
            out += str(file[x])
        if isprime(int(out)):
            print(out)
        
        
collector(digits)
 
