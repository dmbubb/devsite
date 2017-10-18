from codecs import *
from string import *


def rot13Trans(myStr):
    return(encode(myStr, "rot-13"))

def char2Unicode(myStr):
    newstr = ''
    for i in myStr():
        newstr = newstr + ord(i) + " "
    return(newstr)

def Unicode2Char(myStr):
    newstr = ''
    for i in myStr():
        newstr = newstr + chr(i)
    return(newstr)


marStr = str(input("string to decode: "))
newStr = rot13Trans(marStr)
retStr = rot13Trans(newStr)

print("encoded string ", newStr)
print("original string ", retStr)

