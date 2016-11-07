# functions

from turtle import *
  
def mywrite(s):   # my function to write a word
    write(s, font = ("Arial", 18, "bold"))

def spiral(w, c): # my function to print the word w in a spiral, using color c
    pencolor(c)
    for n in range(5,25):
      forward( 4 * n )
      mywrite(w)
      left(92)

# Use the functions -- try the following in console, or un-comment

speed(0)
penup()

# goto(-100,-100)
# spiral("hi", "blue")

# goto(100,-100)
# spiral("fun?", "green")

# goto(-100,100)
# spiral("bye", "red")




# Exercise: finish this function so it makes the turtle
# go to position (x,y) and do the spiral thing for
# the given word and color.
def draw(x, y, word, color):
    print("oops")

