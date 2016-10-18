import string

n = 35
k = 5
#a = []
a = list(string.ascii_letters)

def load_array(n,k):
  for i in range(n):
     a.append(i+1)

def left_shift(k,a):
   for _ in range(k):
      a.append(a.pop(0))
#   print(*a)

#load_array(n,k)
left_shift(k,a)
