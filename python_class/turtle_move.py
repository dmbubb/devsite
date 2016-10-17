import turtle
t = turtle.Pen()
def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)
    t.fillcolor("gray")

max_num_sides = 19 # int(input("How many sides? "))
side_len = 12 # int(input("How long is each side (pixels)? "))
colors = ["darkblue","orange","gray","brown"]
col=1
start_side = 3
incr = 2
my_x = -300
my_y = 300
t.ht()
t.up()
t.setpos(-300,300)
t.st()
t.color(colors[col-1])
for i in range(start_side,max_num_sides,incr):
    t.color(colors[col-1])
    t.write(str(i) + "-gon", font=("Times", 16, "normal"))
    t.sety(my_y)
    my_y = my_y - 40
    if col < 3:
      col+=1
    else:
      col = 0
