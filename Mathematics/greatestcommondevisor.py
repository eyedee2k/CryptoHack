#!/usr/bin/env python3
from gmpy2 import gcdext

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print(gcd(66528, 52920))

print(gcdext(26513, 32321))