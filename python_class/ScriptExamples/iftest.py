import sys

W = "Weird"
NW = "Not Weird"
#
N = int(input("num ").strip())

if (N % 2 == 0):
    if N > 5 and N < 21:
        print(W)
    else:
        print(NW)
else:
    print(W)
