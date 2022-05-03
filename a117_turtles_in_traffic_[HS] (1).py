#%%
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","brown", "yellow", "violet","black","wheat"]

for s in turtle_shapes:
  Harit = trtl.Turtle(shape=s)
  my_turtles.append(Harit)

# starting variables
startx = 0
starty = 0
n = 0

# movement / main code
for Harit in my_turtles:

  # color change in the main code
  new_color = turtle_colors.pop()
  Harit.fillcolor(new_color)

  # the code will start in the middle and then move out 
  Harit.pu()
  Harit.goto(startx, starty)
  Harit.pd()
  Harit.right(n)
  Harit.forward(100)
  
  n += 36 # change the turn radius
  
  # shape will go to the middle, and then through the code (for Loop) again
  startx = Harit.xcor()
  starty = Harit.ycor()

wn = trtl.Screen()
wn.mainloop()
#%%