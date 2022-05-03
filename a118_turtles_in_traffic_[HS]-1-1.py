#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
#%%
import turtle as trtl
screen = trtl.Screen()

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.pu()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.pu()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto(-tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

# starting variables
x = 0
steps = 0
# tloc = 300

# main code
while steps < 100:
    steps += 1 # incrementing by 1
    for ht in horiz_turtles:
        for vt in vert_turtles:

            # the speed of the shapes, using "steps"
            ht.forward(steps) 
            vt.forward(steps)

            if (abs(ht.xcor() - vt.xcor()) < 30): # check for collision in the X value
                if (abs(ht.ycor() - vt.ycor()) < 30): # check for collision in the Y value

                    # when hit, the shapes will turn the color red
                    ht.fillcolor("red") 
                    # vt.fillcolor("red")

                    # after the color turns red, the shape will bounce back
                    while (x < 10): # collison response
                        ht.forward(-3)
                        vt.forward(3)
                        x += 1
                    x = 0

                    # following the bounce effect, the robot will return to the orgin and change shape
                    vt.goto(0,50) # 50 off Y orgin
                    ht.goto(50,50) # 50 off X orgin and 50 off the Y orgin
                    vert_turtles.remove(vt)
                    horiz_turtles.remove(ht)
                
                    # ALT OUTCOME BELOW 

                    # following the bounce effect, the robot will return to the orgin
                    # vt.goto(-tloc, 350)
                    # vert_turtles.remove(vt)
                    # ht.goto(-350, tloc)
                    # horiz_turtles.remove(ht)
                    # tloc -= 50

# when the program is complete, the code below will display a message!
trtl.color('black')
style = ('Courier', 30, 'italic')
trtl.write("The program is complete!", font=style, align='center')
trtl.hideturtle()

# same code from up above, but in 'print' form
print("The program is complete!")


                    
wn = trtl.Screen()
wn.mainloop()
# %%
