# Pie chart of daily activities - exercise 
from turtle import *

# input the daily sleep, school, and screen hours
sleep = int(input("how much sleep per day? "))
school = int(input("hours of school? " ))
screen =int(input("screen time? " ))

# Check whether the hours are reasonable; if not, change
# the variables be 8 sleep, 6 school, and 2 screen.
if sleep + school + screen > 24:
    sleep = 8
    school = 6
    screen = 2

# angles of pie slices 
sleepZ = sleep/24 * 360
schoolZ = "TO DO"
screenZ = "TO DO"

# colors of pie slices
sleepC = "blue"
schoolC = "TO DO"
screenC = "TO DO"

# prepare to draw slices
radius = 100
goto(0,0)

# draw the sleep slice
#     From center, go to edge, draw arc, return to center


# draw the legend
penup()
f = ("Times", 24, "normal")
goto(-130,130)
setheading(0)
color(sleepC)
write("sleep", font=f)

# TO DO: the other legends







    
