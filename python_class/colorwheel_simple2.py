import turtle
import sys
from math import pi

###### new ideas
#"{0:.1f}".format(etc_percent * 100)
#
###### general vars
day_hours = 24.0
activity_hours = 0
rem_hours = day_hours
rem_percent = 0
error_msg = "A day has only 24 hours; your time spent on activites is greater than that. Please retry."
###### vars for writing Legend
writing_x = -375
writing_y = 200
###### vars fro writing circle
heading = 90
radius = 150
circle_x = 100
circle_y = 0
start_angle = 0
ang = [40,75,80,62,23]
cols = ["SteelBlue", "tomato", "palegreen", "orange", "brown"]
a = 0

#
###### #
######
t = turtle.Pen()
t.clear()
t.color("black")
t.pu()
t.goto(0,-150)
t.seth(0)
t.pd()
t.fillcolor("snow")
t.begin_fill()
t.circle(150)
t.end_fill()
t.pu()
t.home()
t.pd()
t.fd(150)
t.pu()
t.home()
t.pd()
for c in range(len(cols)):
  t.color(cols[c])
  b = a
  a = a + ang[c]
  #print(str(c) + " " + str(a))
  for i in range(b,a,4):
     #print(" - " + str(i))
     t.seth(i)
     t.fd(150)
     t.home()
    




#
#######
t.ht()
