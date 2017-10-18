import sys
import random

#s,t = input().strip().split(' ')
#s,t = [int(s),int(t)]
#a,b = input().strip().split(' ')
#a,b = [int(a),int(b)]
#m,n = input().strip().split(' ')
#m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
#

a = 25955
s = 45626
t = 74469
b = 88171



#
apple_num = 0
orange_num = 0
for i in range(len(apple)):
    a_pos = a + apple[i]
    if a_pos >= s and a_pos <= t:
        apple_num += 1
        
for i in range(len(orange)):
    o_pos = b + orange[i]
    if o_pos <= b and o_pos >= s:
        orange_num += 1

print(apple_num)
print(orange_num)
