teststr = "wwejfpwejfpweaaaaamvdmVirknafnbbbbbaSpfjpsfjienfdfidcfjfbnsdjfcCcccc"


def findDup(myStr):
    res = ""
    res_str = ""
    dup_cnt=1
    for i in range(len(myStr)-1):
        if myStr[i] == myStr[i+1]:
            dup=True
            while (dup == True):
                #print("dupe loop")
                if (i == len(myStr)-1) or (myStr[i] != myStr[i+1]):
                    dup=False
                else:
                    i += 1
                    dup_cnt += 1
                    
            res_str = myStr[i] + str(dup_cnt)
            dup_cnt=1
        else:
            res_str = myStr[i]
            #print("sing")
            
        res = res + res_str
    return res

print(findDup(teststr))
