#!/usr/bin/env python3
from math import *
from random import *

#N = float(input("Temp in Celsius ").strip())
temperatures=[10,-20,-289,100]
fileses=["f1","f2","f3"]

def c2f(cDeg):
    if cDeg >= -273.15:
        fahren = (cDeg * 9/5) + 32
        return fahren
    else:
        #errmsg="Temperature must be greater than 273.15"
        #return errmsg
        pass




with open("/tmp/templist.txt","w+") as file:
    for i in temperatures:
        file.write(str(c2f(i))+"\n")
        #print(c2f(i))


for i in range(48):
    filestr="/tmp/tst1/f"+str(randint(0,2))+".txt"
    with open(filestr,"a+") as file:
        file.write(str(randint(50,10000)/randint(2,19))+"\n")
