
num_range = int(input("number range? "))
primelist = [2]
num_hold = []


def numberlist(n):
    numlist = []
    for i in range(n):
        numlist.append(i+1)
    return(numlist)
    
def primeget(nlist):
    num_hold = []
    for i in range(len(nlist)):
        if nlist[i] > primelist[len(primelist)-1] and nlist[i] % primelist[len(primelist)-1] != 0:
            num_hold.append(nlist[i])
    print("num_hold ", num_hold)
    primelist.append(num_hold.pop(0))
    print("primes ",primelist)
    if  len(num_hold) > 0:
        primeget(num_hold)
    return(num_hold)

        

print(primeget(numberlist(num_range)))
