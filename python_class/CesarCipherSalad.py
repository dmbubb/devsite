from codecs import *
from string import *

testr = "The quick brown fox jumped over the lazy dog"
#testr = str(input("string to decode: "))

srcList = ascii_uppercase
#srcList = ascii_letters
#srcList = printable


tstr = testr.upper()


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
    print(rotTrans(tstr,i))

offs = int(len(srcList)/2)
print(offs)
print("original string ", tstr)
firstStr = rotTrans(tstr,offs)
print("first transform ",firstStr)
print("return to orig ",rotTrans(firstStr,offs))

