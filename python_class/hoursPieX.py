# Pie chart of daily activities

from math import pi
from turtle import *

sleep = int(input("how many hours sleep? "))
school = int(input("how many hours in school? "))
screen = int(input("how many hours screen time? "))

if sleep + school + screen > 24:
    print("Impossible hours; using default values.")
    sleep = 8
    school = 6.5
    screen = 2

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
goto(0,0)
left(90)  # so it's aiming upward
right(sleepd)
forward(radius)
backward(radius)
right(schoold)
forward(radius)
backward(radius)
right(screend)
forward(radius)
backward(radius)


    



    
