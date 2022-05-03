#%%
# a121_catch_a_turtle.py

#-----import statements-----

import turtle as trtl
import random as rand

#-----game configuration----

wn = trtl.Screen() # main screen

dot = trtl.Turtle() # main dot to click on
score_writer = trtl.Turtle() # the "turtle" that shows our score
counter = trtl.Turtle() # time count down


dot_sizes = [1,3,5,7,9,11,13] # for the random aspect
# random colors for the background
colors  = ["salmon", "sandybrown", "yellowgreen", "lightseagreen", "cornflowerblue", "mediumpurple", "palevioletred"]

font_setup = ("Verdana", 20, "bold") # the font setup 

# starting values
score = 0 
x_pos = 0
y_pos = 0
timer = 30
counter_interval = 1000
timer_up = False 
dotsize = 3


# displaying the counter and score texts
counter.penup()
counter.hideturtle()
counter.goto(-200,185)
dot.penup()
score_writer.penup()
score_writer.hideturtle()
score_writer.color("snow")
score_writer.goto(-200,160)


#-----initialize turtle-----

# the turtle shaped like a dot will use a global variable

dot.goto(0,0)
dot.shape("circle")
dot.color("deeppink")
dot.shapesize(2)

#-----game functions--------


# teleporting the dot
def teleport_dot(x,y):
  dot.hideturtle()
  global x_pos
  global y_pos
  x_pos = rand.randint(-400, 400) #RANDOM
  y_pos = rand.randint(-300, 300)
  dot.goto(x_pos,y_pos)
  dot.showturtle() # after moving, dot will come back

    
#basic timer (countdown method)
def countdown():
  global timer, timer_up
  global dotsize
  counter.clear()
  if timer <= 0: # if the timer hits 0, game finishes
    counter.write("GAME OVER!", font=font_setup)
    timer_up = True
    dot.hideturtle()
  else: # if not 0, timer will continue to go down
    counter.write("Time Left: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
    dotsize += 0.5
    dot.shapesize(dotsize)


# when ever you click on a dot, score will increase
def update_score():
  global score
  score += 1
  print(score)
  score_writer.clear()
  score_writer.write ("Your Score: " + str(score), font=font_setup)


# uses the functons created before, and combinds them
def dot_clicked(x,y):
    global timer
    global dotsize
    if(timer >= 0): # if clicked, dot will get smaller
      update_score()
      teleport_dot(x,y)
      dotsize -= 1
      dot.shapesize(dotsize)
    else:
      dot.hideturtle()

# the MAIN start game function
def start_game():
  for count in range(50): 
    color = rand.choice(colors) # Choose a random color
    wn.bgcolor(color) 
  countdown()
  dot.onclick(dot_clicked)


#-----events----------------


# MAIN EVENT
start_game()

wn.mainloop()
#%%