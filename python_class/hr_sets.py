import sys
#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]
#a = [int(a_temp) for a_temp in input().strip().split(' ')]
#b = [int(b_temp) for b_temp in input().strip().split(' ')]

n,m = 2,3
a = [2,4]
b = [16,32,96]
# 4 8 16
dd = [2, 4, 8, 2, 4, 8, 16, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48]

def getFactor(N):
    factor_list = []
    for i in range(2,int((N/2)+1)):
        if N % i == 0:
            factor_list.append(i)
    return(factor_list)

def chkFactorB(b_list):
    d = []
    for j in range(len(b_list)):
        d.extend(getFactor(b_list[j]))
    #d_set = set(d)
    return(d)


def chkFactorA(d_list,a_list):
    pop_list = []
    for j in range(len(d_list)):
        for k in range(len(a_list)):
            if d_list[j] % a_list[k] == 0:
                print(d_list[j])
 #               pop_list.append(j)
    return(pop_list)

#print(chkFactorB(b))
#dlist = chkFactorB(b)
print(chkFactorA(dd,a))

