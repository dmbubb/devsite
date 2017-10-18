import turtle

#colors = ['#880000','#884400','#888800','#008800',
#          '#008888','#000088','#440088','#880088']

colors = ['cyan', '#00bb00','#bb0000','gray','orange']
activity = ["sleeping", "eating", "playing", "studying", "etc."]
hours = []
day = 24.0
tot_hours = 0
for i in range(len(activity)-1):
    hours.append(float(input("How many hours spent " + activity[i] + "?")))
    tot_hours = hours[i] + tot_hours
    rem_hours = day - tot_hours
    print("remaining hours are ", str(rem_hours))
    if tot_hours > 24:
        print("total hours cannot exceed 24")
        exit
hours.append(rem_hours)
tur = turtle.Pen()
def day_color_wheel(colors, radius, center=(0, 0)):
#   slice_angle = 360 / len(activity)
    heading, position = 90, (center[0] + radius, center[1])
    loops = 0
    init_x = -275
    init_y = 175
    tur.penup()
    tur.setpos(init_x,init_y+25)
    tur.write("Activities and percent of day", font=("Times", 24, "normal"))
    for color in colors:
#        tur.color("black")
        tur.color(color, color)
        tur.penup()
        tur.setpos(init_x,init_y)
        activity_percent = hours[loops]/day
        slice_angle = 360 * (activity_percent)
        tur.write(str(hours[loops]) + " hours spent " + activity[loops] + " " + "{0:.2f}".format(activity_percent * 100) + "% of day", font=("Times", 16, "normal"))
#        print(activity[loops])
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

day_color_wheel(colors, 150, center=(25, 50))
tur.hideturtle()
