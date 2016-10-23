import sys
import os


#teststr = "wwejfpwejfpweaaaaamvdmVirknafnbbbbbaSpfjpsfjienfdfidcfjfbnsdjfcCcccc"

 
def  compress(strr):
    ins_char = ""
    res = ""
    reslist = []
    start = 0
    for i in range(len(strr)-1):

        if strr[i] == strr[i+1]:
            start += 1
            ins_char = strr[i]+str(start+1)
        else:
            start = 0
            ins_char = strr[i]

        reslist.append(ins_char)
             
    
    
    res = str(reslist)
    return res


def locateDupe(myStr):
    for _


print(str(compress(teststr)))
