from random import *
a = []
dimen1 = 6
dimen2 = dimen1
limit = dimen1 - 2
s = []
#

for _ in range(dimen1):
    a_tmp = []
    for _ in range(dimen2):
        a_tmp.append(randint(-9,9))
    a.append(a_tmp)
#   print(a[i])

for j in range(limit):
    for i in range(limit):
        print(str(j) + " " + str(i))
        sum = (a[j][i] + a[j][i + 1] + a [j][i +2] + a[j+1][i + 1] + a[j+2][i] + a[j+2][i + 1] + a [j+2][i +2])
        s.append(sum)

#print(s)
print(max(s))

        
