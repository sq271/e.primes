#!/bin/python

# ecalc.py

import decimal
decimal.getcontext().prec = 10000

fact = 1
euler = 2

for x in range(2, 150):
    fact *= x
    euler += decimal.Decimal(str(1.0))/decimal.Decimal(str(fact))

print(euler)
