#   a114_robot_maze.py
import turtle as trtl

#------ robot algorithms
def move():
  robot.dot(10)
  robot.forward(50)

def turn_left():
  robot.speed(0)
  robot.left(90)
  robot.speed(2)

def turn_right():
  k = 0
  while(k < 3):
    k += 1
    turn_left()

#----- roboto starting location
startx = -100
starty = -100

#----- init screen
wn = trtl.Screen()
wn.setup(width=400, height=420)

#----- init robot
robot_image = "Spaceship1.png"
wn.addshape(robot_image)
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.penup()
robot.pencolor("darkorchid") # used for dot color
robot.setheading(90)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO 1: change maze here
wn.bgpic("Space1.jpg") # other file names should be maze2.png, maze3.png

#---- TODO 2: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()

I = 0 

# move the robot four spaces
while (I < 4): 
  I += 1
  move()
  robot.dot(10)

# turn right / defined previously
turn_right()

# move the robot four spaces
L = 0
while (L < 4): 
  L += 1
  move()





#---- end robot movement 

wn.mainloop()
