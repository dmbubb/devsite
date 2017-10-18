from codecs import *
from string import *
from math import *

testr = "The quick brown fox jumped over the lazy dog"
#testr = str(input("string to decode: "))

srcList = ascii_uppercase
#srcList = ascii_letters
#srcList = printable

tstr2 = 'GUR DHVPX OEBJA SBK WHZCRQ BIRE GUR YNML QBT'
tstr = testr.upper()

def caesarShift(offset):
    cshift = ''
    orig = ''
    for i in range(len(ascii_uppercase)):
        newind = (i + offset) % len(ascii_uppercase)
        orig = orig + " | " + ascii_uppercase[i]
        cshift = cshift + " | " + ascii_uppercase[newind]
    print("offset is ", offset)
    print(orig)
    print(cshift)

def rotTrans(myStr,offset):
    newstr = ''
    for i in tstr.strip():
        if i in srcList:
            thisind = (srcList.find(i) + offset) % len(srcList)
            newstr = newstr + srcList[thisind]
            #print(newstr)
        else:
            newstr = newstr + i
            #print(newstr)
    return(newstr)


for i in range(len(srcList)):
    print("ROT ",i)
    print(rotTrans(tstr2,i))

#offs = int(len(srcList)/2)
#print(offs)
#print("original string ", tstr)
#firstStr = rotTrans(tstr,offs)
#print("first transform ",firstStr)
#print("return to orig ",rotTrans(firstStr,offs))

