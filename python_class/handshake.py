import sys

#T is number of inputs
#N is a number of folks

T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    sum = 0
    for i in range(N):
        sum += i
    print(sum)
