import turtle
t = turtle.Pen()
t.begin_fill()
t.color("red")
for _ in range(4):
    t.fd(100)
    t.rt(90)
t.end_fill()
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
   tur.up()
   tur.backward(6*i)
   tur.left(90)
   tur.forward(300)
   tur.down()
   tur.begin_fill()
   tur.color(col)
   drawPolygon(tur, side_len, i)
   tur.end_fill()
   if col < 3:
      col+=1
   else:
      col = 0
