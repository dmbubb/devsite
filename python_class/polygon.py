import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)
    t.fillcolor("gray")

max_num_sides = int(input("How many sides? "))
side_len = int(input("How long is each side (pixels)? "))
tur = turtle.Pen()
tur.up()
tur.left(90)
tur.forward(250)
tur.right(90)
tur.down()
#colors = ["red","darkblue","darkgreen","orange","gray","purple","magenta","cyan","brown"]
colors = ["darkblue","orange","gray","brown"]
col=1
start_side = 3
incr = 2
for i in range(start_side,max_num_sides,incr):
   tur.up()
   tur.backward(300)
   tur.right(90)
   tur.forward(6*i)
   #tur.color("darkgray")
   tur.color(colors[col-1])
   tur.down()
   tur.write(str(i) + "-gon", font=("Times", 16, "normal"))
 #  tur.up()
   tur.backward(6*i)
   tur.left(90)
   tur.forward(300)
   tur.down()
   tur.begin_fill()
   tur.color(colors[col-1])
   drawPolygon(tur, side_len, i)
   tur.end_fill()
   if col < 3:
      col+=1
   else:
      col = 0
tur.up()
tur.right(90)
tur.forward(250)
tur.down()
tur.color("blue")
tur.write("Approximating a circle (1 pixel - 360 'sides')", font=("Times", 16, "normal"))
drawPolygon(tur, 1, 360)
tur.up()
#tur.right(90)
tur.forward(250)
tur.down()
tur.color("darkgreen")
tur.write("Approximating a circle using built in function", font=("Times", 16, "normal"))
tur.circle(75,None,None)
tur.ht()
