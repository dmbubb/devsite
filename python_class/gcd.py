import sys


def gcdFind(a,b):
    while b != 0:
       r = a % b
       a = b
       b = r
    return(a)

print(gcdFind(2346, 342))
