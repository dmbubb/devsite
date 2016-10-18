# Pie chart of daily activities

from math import pi
from turtle import *

# Add code to input the daily sleep, school, and screen hours
#sleep =
#school =
#screen =

# Check whether the hours are reasonable; if not, change them
#......

# convert hours/24  into  degrees/360
m = 360/24
sleepd = m * sleep
schoold = m * school
screend = m * screen

# draw circle centered at (0,0)
radius = 100
circumf = 2 * pi * radius
seg = circumf / 360 # size of one segment of circle
penup()
goto(0,radius)      # start at top of circle
pendown()
for i in range(360):
    forward(seg)
    right(1)

# draw pie pieces
#.........
