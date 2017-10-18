from turtle import *

#
#input variables
sleep = int(input("how much sleep per day? "))
school = int(input("hours of school? " ))
screen =int(input("screen time? " ))
etc = 24 - (sleep + school + screen)
#
# main vars
acts = [sleep, school, screen, etc]
names = ["sleep","school","screen","other things"]
cols = ["green", "cyan", "orange", "gray"]
radius=120
f = ("Times", 24, "normal") # font for writing
write_x = -130
write_y = 220
offset = 0

for i in range(len(acts)): 
  ang = acts[i]/24 * 360
  offs = offset/24 * 360
  color(cols[i])
  fillcolor(cols[i])
  penup()
  goto(write_x,write_y)
  setheading(0)
  write(names[i], font=f)
  home()
  pendown()
  left(offs)
  begin_fill()
  forward(radius)
  left(90)
  circle(radius, ang)
  home()
  end_fill()
  write_y = write_y - 30
  offset = offset + acts[i]
