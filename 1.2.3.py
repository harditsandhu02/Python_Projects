import turtle as trtl
import random as rand
from random import randint

apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"


#setup
wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=0.5, height=0.5)
wn.bgpic("background.gif")


#variables
apple = trtl.Turtle()
drawer = trtl.Turtle()

drawer.ht()
# given a turtle, set that turtle to be shaped by the image file
apple.pu()

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

draw_apple(apple)

def apple_down():
  A = apple
  A.showturtle()
  drawer.pu()
  A.goto(randint(-100,100),randint(0,240))
  while(A.ycor() > -150):
    A.sety(A.ycor() - 6)

  if (A.ycor() < -149):
    A.hideturtle()
#apple_down(apple)


# This function takes care of font and color.
def draw_an_A():
  drawer.pu()
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold"))
  drawer.goto(apple.xcor()-11,apple.ycor()-36) 
  draw_apple(apple)


wn.onkeypress(apple_down,"a")

wn.listen()

trtl.mainloop()