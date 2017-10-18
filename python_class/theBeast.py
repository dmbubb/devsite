import sys
from random import *

three5s = "555"
five3s = "33333"


def num_string(div,num,mult):
  numstr = str(num)
  for i in range(1,div):
    numstr = numstr + str(num)*mult
  return numstr
    
    

def dec_num(n):
  print(" checking... ", n)
  div3 = n // 3
  rem3 = n % 3
  div5 = n // 5
  rem5 = n % 5
  fives = -1
  threes = -1
  if rem3 != 0:
    if rem5 == 0:
      threes = div5
      fives=0
    elif rem3 == 2:
      fives = div3 - 1
      threes = 5
  else:
    fives = div3
    threes = 0
    
  if fives != -1 and threes != -1:
    fivestr = num_string(div3,5,3)
    threestr = num_string(div5,3,5)
    allstr = fivestr+threestr
#    print(allstr)
#    print(len(allstr))
#    print(len(fivestr))
#    print(len(threestr))
  else:
    print("not a decent number")
      
  



  
dec_num(159)

#t = int(input().strip())
#for a0 in range(t):
#    n = int(input().strip())


for i in range(randint(1,20)):
  nn = randint(1,1000)
#  dec_num(nn)
