#!/bin/python

# mkprimes.py

def isprime(a):
    if a % 2 != 0:
        return all(a % i for i in range(3,a,2))


for i in range(3,1000000):
    if isprime(i):
        print(i)


