import random
x = 25
y = -200
z = 20

n = int(input())
#s = "35 30 18 16 12 33 33 25 22 3 29 6 12 17 26"
#s = "57 57 -57 57"
s = str(input()).split(" ")
t = tuple(s)
def numpiler(x,y,z):
  numlist = []
  for _ in range(x):
    numlist.append(random.randint(y,z))
  numtup=tuple(numlist)
  #print(numlist)
  return(numtup)

def findbig(t):
    hold_list = []
    f = []
    for i in t:
        if i not in hold_list:
            hold_list.append(int(i))
            
    f = sorted(hold_list, reverse=True)
    print(f)
    print(f[1])
            
    
    #print(t)
    #print(hold_list)
    #
        
 
#t = numpiler(x,y,z)
findbig(t)
