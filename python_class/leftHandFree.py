n = 5
k = 4
a = [1,2,3,4,5]
def left_shift(n,k,a):
   for _ in range(k):
      tmpa = a.pop(0)
      a.append(tmpa)
# following dewsnt work for 2.7
   print(*a)

left_shift(n,k,a)
#answer = left_shift(n,k,a);
#print(*answer, sep=' ')
