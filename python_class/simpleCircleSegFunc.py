import turtle
t = turtle
#
#main variables
sleep = int(input("how much sleep per day? "))
school = int(input("hours of school? " ))
screen =int(input("screen time? " ))
etc = 24 - (sleep + school + screen)

#color vars
sleep_col = "green"
school_col ="cyan"
screen_col = "orange"
etc_col = "gray"
sleep_lcol = "green"
school_lcol = "blue"
screen_lcol = "red"
etc_lcol = "darkgray"
#
# function
#
def drawSeg(activity, col, lcol, offset):
  ang = activity/24 * 360
  offs = offset/24 * 360
  t.color(col)
  t.fillcolor(lcol)
  t.penup()
  t.goto(write_x,write_y)
  t.setheading(0)
  t.write(act_str, font=f)
  t.home()
  t.pendown()
  t.left(offs)
  t.begin_fill()
  t.forward(radius)
  t.left(90)
  t.circle(radius, ang)
  t.home()
  t.end_fill()

#general variables
radius=120
f = ("Times", 24, "normal") # font for writing
write_x = -130
write_y = 220
act_str = "sleep"
offset = 0
drawSeg(sleep, sleep_col, sleep_lcol, offset)
#
write_y = write_y - 30
act_str = "school"
offset = offset + sleep
drawSeg(school, school_col, school_lcol, offset)
#
write_y = write_y - 30
act_str = "screen"
offset = offset + school
drawSeg(screen, screen_col, screen_lcol, offset)
#
write_y = write_y - 30
act_str = "other things"
offset = offset + screen
drawSeg(etc, etc_col, etc_lcol, offset)
