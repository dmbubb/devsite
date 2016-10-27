from random import *
a = []
dimen1 = 6
dimen2 = dimen1
pad = " "
s = ""
#
for _ in range(dimen1):
    a_tmp = []
    for _ in range(dimen2):
        a_tmp.append(randint(1,9999)%2)
    a.append(a_tmp)



for i in range(len(a)):
    print(join(a, sep=' '))

