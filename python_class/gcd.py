import sys
a = 457 * 17 * 7 * 21
b = 49 * 25 *3 * 17

while b != 0:
   r = a % b
   a = b
   b = r
   
print("GCD ", a)
