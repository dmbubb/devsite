import string
import math
import random

a = ""
b = ""
numneed = 0
lc = string.ascii_lowercase


for i in range(random.randint(1,500)):
    x = lc[random.randint(0,len(lc)-1)]
    a = a + x
for i in range(random.randint(1,500)):
    x = lc[random.randint(0,len(lc)-1)]
    b = b + x
#

# following for testing purposes
#a = "mkzntqmkpyhhtmmgdljatcbmddlnbyxlnruyij"
#b = "dtdmoxxxhotqklzcouzjmdlrpgwwmqkgccgn"
#b = a
#b = a[::-1]


def number_needed(a,b):
  numneed = 0
  alist = list(a)
  blist = list(b)
  alist.sort()
  blist.sort()
  
  if alist == blist:
      exit
  else:
      for j in lc:
          numneed = numneed + abs(alist.count(j) - blist.count(j))
  return(numneed)         



#
###
#
print(number_needed(a,b));





