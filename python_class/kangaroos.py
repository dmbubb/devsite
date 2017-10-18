import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
kmesg = "NO"
x_diff = abs(x2-x1)
old_diff = x_diff +1
while x_diff < old_diff:
    old_diff = x_diff
    print(x_diff)
    x1 += v1
    x2 += v2
    if x_diff == 0:
        kmesg = "YES"
        break
    x_diff = abs(x2-x1)
    
print(kmesg)    

