import sys
import random

apple = []
orange = []
appnum = 150
ornum = 120
a = 25955
s = 45626
t = 74469
b = 88171


adiff = t - a 
bdiff = b - s

for _ in range(appnum):
  apple.append(random.randint((-1*adiff),adiff))
  
for _ in range(ornum):
  orange.append(random.randint((-1*bdiff),bdiff))

#
# a < s < t < b
#
apple_num = 0
orange_num = 0
for i in range(len(apple)):
    a_pos = a + apple[i]
    if a_pos >= s and a_pos <= t:
        apple_num += 1
        
for i in range(len(orange)):
    o_pos = b + orange[i]
    if o_pos >= s and o_pos <= t:
        orange_num += 1

print(apple)
print(orange)
print(apple_num)
print(orange_num)
