import turtle
tur = turtle.Pen()

tur.clear()
radius = 150
angs = [72,120,48,80,40]
cols = ["orange","blue","gray","green","darkred"]

def circleSegs(cols,angs):
  for i in range(len(angs)):
  	tur.penup()
  	tur.home()
  	tur.color(cols[i])
  	tur.forward(radius)
  	tur.begin_fill()
  	
  	tur.circle(radius,angs[i])
  	tur.end_fill()

tur.ht()

circleSegs(cols,angs)
