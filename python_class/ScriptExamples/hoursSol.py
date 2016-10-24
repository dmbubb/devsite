# Pie chart of daily activities - SAMPLE SOLUTION
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
schoolZ = school/24 * 360
screenZ = screen/24 * 360

# colors of pie slices
sleepC = "blue"
schoolC = "red"
screenC = "purple"

# prepare to draw slices
radius = 100
#speed(1)
showturtle()
goto(0,0)

# def piece(colr, portion):

# sleep slice
begin_fill()
color(sleepC)
forward(radius)
left(90)
circle(radius,sleepZ)
goto(0,0)
right(90)
end_fill()

# school slice
begin_fill()
color(schoolC)
forward(radius)
left(90)
circle(radius,schoolZ)
goto(0,0)
right(90)
end_fill()

# screen slice
begin_fill()
color(screenC)
forward(radius)
left(90)
circle(radius,screenZ)
goto(0,0)
right(90)
end_fill()

# draw the legend
penup()
f = ("Times", 24, "normal")
goto(-130,130)
setheading(0)
color(sleepC)
write("sleep", font=f)
forward(80)
color(schoolC)
write("school", font=f)
forward(80)
color(screenC)
write("screen", font=f) 








    
