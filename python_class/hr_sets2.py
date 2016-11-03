import sys
#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]
#a = [int(a_temp) for a_temp in input().strip().split(' ')]
#b = [int(b_temp) for b_temp in input().strip().split(' ')]

n,m = 2,3
a = [2,4]
b = [16,32,96]
# 4 8 16
aIsFactOf = []
factorOfB = []
for j in range(len(b)):
    N = b[j]
    for i in range(2,int((N/2)+1)):
        if N % i == 0:
            factorOfB.append(i)
factorOfB_set = set(factorOfB)

print("factors of B:")
print(factorOfB_set)

#   d.extend(getFactor(b[j]))


for j in range(len(factorOfB)):    
    for k in range(len(a)):
        factt = True
        if factorOfB[j] % a[k] != 0:
            factt = False
        #print(factt)
    if factt == True:
        #print("add " + str(factorOfB[j]))
        aIsFactOf.append(factorOfB[j])
aIsFactOf_set = set(aIsFactOf)
print("A is factor of :")
print(aIsFactOf_set)
bothTrue = aIsFactOf_set & factorOfB_set 
print(bothTrue)
