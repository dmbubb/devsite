import turtle
import sys

###### new ideas
#"{0:.1f}".format(etc_percent * 100)
#
###### general vars
day_hours = 24.0
activity_hours = 0
rem_hours = day_hours
rem_percent = 0
error_msg = "A day has only 24 hours; your time spent on activites is greater than that. Please retry."
###### vars for writing Legend
writing_x = -375
writing_y = 200
###### vars fro writing circle
heading = 90
radius = 150
circle_x = 100
circle_y = 0
#
###### Sleep hours
sleep_hours = float(input("How many hours spent sleeping? (" + str(rem_hours) + ") remaining "))
activity_hours = float(activity_hours + sleep_hours)
rem_hours = day_hours - activity_hours
if activity_hours > day_hours:
    print(error_msg)
    sys.exit()
else:
    sleep_percent = "{0:.1f}".format((sleep_hours/day_hours) * 100)
#    sleep_percent = (sleep_hours/day_hours) * 100
###### School hours
school_hours = float(input("How many hours spent at school? (" + str(rem_hours) + ") remaining "))
activity_hours = float(activity_hours + school_hours)
rem_hours = day_hours - activity_hours
if activity_hours > day_hours:
    print(error_msg)
    sys.exit()
else:
    school_percent = "{0:.1f}".format((school_hours/day_hours) * 100)
###### Play hours
play_hours =  float(input("How many hours spent playing? (" + str(rem_hours) + ") remaining "))
activity_hours = float(activity_hours + play_hours)
rem_hours = day_hours - activity_hours
if activity_hours > day_hours:
    print(error_msg)
    sys.exit()
else:
    play_percent = "{0:.1f}".format((play_hours/day_hours) * 100)
    
if rem_hours < day_hours:
    etc_hours = ( day_hours - activity_hours)
    etc_percent = "{0:.1f}".format((etc_hours/day_hours) * 100)

print(str(sleep_percent) + " " + str(school_percent) + " " + str(play_percent) + " " + str(etc_percent))
#
tur = turtle.Pen()
###### print header
tur.penup()
tur.setpos(writing_x,writing_y)
tur.write("Activities and percent of day", font=("Times", 24, "normal"))
#
###### print sleeping info
#tur.penup()
tur.pendown()
tur.color("blue")
tur.setpos(writing_x,writing_y-25)
tur.write(str(sleep_hours) + " hrs spent  spent sleeping: " + str(sleep_percent) + "% of the day", font=("Times", 16, "normal"))
slice_angle = 360 * (float(sleep_percent)/100)
tur.setpos(circle_x,circle_y)
tur.setheading(heading)
#tur.pendown()
tur.begin_fill()
tur.circle(radius, extent=slice_angle)
tur.goto(circle_x,circle_y)
#tur.penup()
tur.setheading(heading)
tur.setpos(circle_x,circle_y)
tur.end_fill()
#
###### print school info
tur.penup()
tur.color("green")
tur.setpos(writing_x,writing_y-50)
tur.write(str(school_hours) + " hrs spent at school: " + str(school_percent) + "% of the day", font=("Times", 16, "normal"))
slice_angle = 360 * (school_percent)
#
###### print playing info
tur.penup()
tur.color("orange")
tur.setpos(writing_x,writing_y-75)
tur.write(str(play_hours) + " hrs spent playing: " + str(play_percent) + "% of the day", font=("Times", 16, "normal"))
slice_angle = 360 * (play_percent)

#
###### print 'etc' info
tur.penup()
tur.color("gray")
tur.setpos(writing_x,writing_y-100)
if etc_hours > 0:
    tur.write("Percent of the day spent on other things: " + str(etc_percent) + "%", font=("Times", 16, "normal"))
    slice_angle = 360 * (etc_percent)

    
#
###### 

#
#######
tur.ht()
