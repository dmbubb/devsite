import turtle
tur = turtle.Pen()
# general vars
colors = ['cyan', '#00bb00','#bb0000','gray','orange']
activities = ["sleeping", "eating", "playing", "studying", "on etc."]
hours = []
day = 24.0
# load hours
#
def load_activity_hrs(activities,hours):
  tot_hours = 0
  for i in range(len(activities)-1):
      hours.append(float(input("How many hours spent " + activities[i] + "? ")))
      tot_hours = hours[i] + tot_hours
      rem_hours = day - tot_hours
      print("remaining hours are ", str(rem_hours))
      if tot_hours > 24:
          print("total hours cannot exceed 24")
          exit
  hours.append(rem_hours)
# set colorwheel
def day_color_wheel(colors, radius, center=(0, 0)):
    heading, position = 90, (center[0] + radius, center[1])
    loops = 0
    init_x = -275
    init_y = 175
    tur.penup()
    tur.setpos(init_x,init_y+25)
    tur.write("Activities and percent of day", font=("Times", 24, "normal"))
    for color in colors:
        tur.color(color, color)
        tur.penup()
        tur.setpos(init_x,init_y)
        activities_percent = hours[loops]/day
        slice_angle = 360 * (activities_percent)
        tur.write(str(hours[loops]) + " hours spent " + activities[loops] + " " + "{0:.2f}".format(activities_percent * 100) + "% of day", font=("Times", 16, "normal"))
#        print(activities[loops])
#        print(slice_angle)
#        print(loops)
        tur.penup()
        tur.goto(position)
        tur.setheading(heading)
        tur.pendown()
        tur.begin_fill()
        tur.circle(radius, extent=slice_angle)
        heading, position = tur.heading(), tur.position()
        tur.penup()
        tur.goto(center)
        tur.end_fill()
        loops = loops + 1
        init_y = init_y - 25
#        
load_activity_hrs(activities,hours)
day_color_wheel(colors, 150, center=(25, 50))
tur.hideturtle()
