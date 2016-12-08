'''
This is a demo task.

A zero-indexed array A consisting of N integers is given.
An equilibrium index of this array is any integer P such that 0 ≤ P < N
and the sum of elements of lower indices is equal to the sum ofelements of higher indices, i.e. 
A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
Sum of zero elements is assumed to be equal to 0.
This can happen if P = 0 or if P = N−1.
'''



test = [-1, 3, -4, 5, 1, -6, 2, 1]

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    for i in range(0,N):
        equil = []
        eq = -1
        low_sum = 0
        high_sum = 0
        print("index ",i)
        for j in range(0,i):
            low_sum = low_sum + A[j]
        for k in range(i+1,N):
            high_sum = high_sum + A[k]
        print("  low ",low_sum)
        print("  high",high_sum)
        if high_sum == low_sum:
            print("*** equil ***")
            #equil.append(i)
            eq = i

    return(eq)

solution(test)
