def fibonacci(n):
    sum = 0
    slist =[0,1]
    for i in range(n):
        sum = slist[-1] + slist[-2]
        slist.append(sum)
        #print(slist[i])
    return slist[n]
    
n = int(input())
print(fibonacci(n))
