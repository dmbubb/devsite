import sys
import random

primelist = [2]
numpool =[]
for i in range(3,100):
    numpool.append(i)

j = 0
while len(numpool) > 0:
    while j < len(numpool):
        if numpool[j] % primelist[-1] == 0:
            print(numpool[j])
            print(len(numpool))
            numpool.remove(numpool[j])
            j += 1
        primelist.append(numpool[j])
 

print(primeist)
        
    
    
