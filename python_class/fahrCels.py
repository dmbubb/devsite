#!/usr/bin/env python3
from math import *

#N = float(input("Temp in Celsius ").strip())
temperatures=[10,-20,-289,100]

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
