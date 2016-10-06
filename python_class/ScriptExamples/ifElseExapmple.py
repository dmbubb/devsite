import sys

W = "Weird"
NW = "Not Weird"
N = int(input().strip())

if (N % 2 != 0):
    print(W)
elif N >= 6 & N <20:
    print(W)
else:
    print(NW)
