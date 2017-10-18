#
# find me at http://mbubb.devio.us/python_class/simplePoly.py
#
from turtle import *
from random import *

color_list=["red", "green", "blue", "yellow", "gray", "cyan"]

def drawPolygon(sideLength, numSides, color):
    turnAngle = 360 / numSides
    fillcolor(color)
    begin_fill()
    for i in range(numSides):
        forward(sideLength)
        right(turnAngle)
    end_fill()
#print(randint(0,5))
#drawPolygon(30,12,"lightgreen")
#drawPolygon(25,16, "cyan")

#for i in range(???):
#  len = ???
#  angle = ???
# goto ???
#  drawPolygon(len,ang,color_list[randint(0,5)])
