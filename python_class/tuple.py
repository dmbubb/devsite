import random
x = 15
y = 2
z = 35

def numpiler(x,y,z):
  numlist = ""
  for _ in range(x):
    if numlist == "":
      numlist = numlist + str(random.randint(y,z)).split(" ")
  numtup=tuple(numlist)
  print(numlist)
  print(numtup)
 

def findbig(t):
    bigger=0
    for i in t:
        if int(i) > int(bigger):
            bigger = i
    return(bigger)
        
t = numpiler(x,y,z)
biggest = findbig(t)
print(t)
print(biggest)
