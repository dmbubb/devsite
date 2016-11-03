from turtle import *

colors=["red", "green", "blue", "orange"]
for _ in range(15):
    for x in range(12):
        pencolor(colors[x%4])
        forward(x)
        left(88)

