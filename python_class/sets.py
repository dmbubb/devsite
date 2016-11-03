import sys
import random
#
#All elements in a are factors of x
#x is a factor of all elements in b
#
#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]
#a = [int(a_temp) for a_temp in input().strip().split(' ')]
#b = [int(b_temp) for b_temp in input().strip().split(' ')]

x = 40
y = 9999
z = 120
#
def genSet(x,y,z):
    for i in range(z):
        print(random.randint(x,y))
        
        
#genSet(x,y,z)

primelist = [2]
primepool =[]
for i in range(3,1000):
    primepool.append(i)
    
for i in range(len(primepool)):
    if primepool[i] % primelist[-1] == 0:
        primepool.remove(primepool[i])
        primelist.append(primepool[i])

print(primepool)
        
    
    
