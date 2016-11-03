import sys
#
n,m = 2,3
a = [2,4]
b = [16,32,96]
# 4 8 16
def factorsOf(num_list):
    factorOf = []
    for j in range(len(num_list)):
        N = b[j]
        for i in range(2,int((N/2)+1)):
            if N % i == 0:
                factorOf.append(i)
    factorOf_set = set(factorOf)

    return(factorOf_set)

def xIsFactorOf(factorOf_list,factor_list):
    isFactOf = []
    for j in range(len(factorOf_list)):
        for k in range(len(factor_list)):
            factt = True
            if factorOf_list[j] % factor_list[k] != 0:
                factt = False
        if factt == True:
            isFactOf.append(factorOf_list[j])
    isFactOf_set = set(isFactOf)
    return(isFactOf_set)

#
FactorsOfX = factorsOf(b)
xFactor = xIsFactorOf(list(FactorsOfX),a)

print(FactorsOfX)
print(xFactor)
print(FactorsOfX & xFactor)
