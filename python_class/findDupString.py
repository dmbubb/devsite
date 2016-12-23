teststr = "wwejfpwejfpweaaaaamvdmVirknafnbbbbbaSpfjpsfjienfdfidcfjfbnsdjfcCccccd"


def findDup(myStr):
    dup_cnt=1
    for i in range(len(myStr)-1):
        if myStr[i] == myStr[i+1]:
            dup_char = myStr[i]
            dup_cnt = dup_cnt + 1
            dup_flag = True
        else:
            dup_cnt=1
            dup_flag = False
  
        if dup_flag == False:
            print(dup_char, " ", str(dup_cnt))
        
            
        
        


findDup(teststr)
