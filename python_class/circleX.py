# Introduction to turtle graphics: circle

from turtle import * # tells Python to use turtle graphics

# Draw a circle.

speed(10) # make turtle go fast (but 0 is faster?!)
penup() # pen up, so movement won't leave a trace
color("black") # make it draw in black
dot(1) # draw a dot, one pixel in size

for i in range(360):  # do these steps 360 times
    right(1) # change direction 1 degree
    forward(100) # move out from center
    dot(1) # draw dot on edge of circle
    backward(100) # go back to center

# Question:
# How can we change it to do a full circle with half as many dots?



# Exercise:
# Add to this program so that it also draws
# lines for a pie chart with 5 equal pieces.



# Exercise:
# Add to this program so that it also draws some lines,
# whatever shape you like.
