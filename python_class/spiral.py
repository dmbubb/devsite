# Using a loop and a list to make colorful spiral.
# (Adapted from the book "Teach your Kids to Code".)

from turtle import *

colors = ["red", "yellow", "blue", "green"]   # a list

for x in range(100):
    print("x and its remainder ", x, x%4)
    pencolor( colors[x % 4] )
    forward(x)
    left(91)
    

# Note: in Trinket you can change the print statement to this:
#  print "x and its remainder", x, x%4
