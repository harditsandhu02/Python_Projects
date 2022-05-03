
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

wn = trtl.Screen()
speedy = trtl.Turtle()
score_writer = trtl.Turtle()
ui = trtl.Turtle()
counter = trtl.Turtle()

speedy_sizes = [1, 2, 3, 1, 0.5, 0.8, 1.5]
colors  = ["red", "orange", "yellow", "green yellow", "deep sky blue", "cyan", "medium slate blue"]
font_setup = ("Arial", 20, "normal")

score = 0 
x_pos = 0
y_pos = 0
timer = 5
counter_interval = 1000
timer_up = False  

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

#-----game configuration----
counter.penup()
counter.hideturtle()
counter.goto(-319,268)
speedy.penup()
score_writer.penup()
score_writer.hideturtle()
score_writer.color("blue")
ui.hideturtle()
ui.speed(9)
ui.penup()
ui.goto(327,260)
ui.speed(5)
ui.pendown()
ui.color("slate gray")
ui.begin_fill()
ui.circle(25)
ui.end_fill()
ui.penup()
score_writer.goto(319,268)

#-----initialize turtle-----
# turtle shaped turtle will use a global variable
speedy.goto(0,0)
speedy.shape("turtle")
speedy.color("moccasin")
speedy.shapesize(2)

#-----game functions--------
#background
for count in range(50): 
  color = rand.choice(colors) #Choose a random color
  wn.bgcolor(color) 
    
#timer
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("GAME OVER!", font=font_setup)
    timer_up = True
    speedy.hideturtle()
  else:
    counter.write("Time: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# move speedy
def teleport_speedy(x,y):
    speedy.hideturtle()
    global x_pos
    global y_pos
    x_pos = rand.randint(-400, 400)
    y_pos = rand.randint(-300, 300)
    speedy.goto(x_pos,y_pos)
    speedy.showturtle()
    speedy.shapesize(rand.choice(speedy_sizes))

# update_score
def update_score():
  global score
  score += 1
  print(score)
  score_writer.clear()
  score_writer.write (score,font=font_setup)

def speedy_clicked(x,y):
    global timer
    print("Gotcha!")
    if(timer >= 0):
      timer += 1
      update_score()
      teleport_speedy(x,y)
    else:
      speedy.hideturtle()

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

      
#-----events----------------
countdown()
speedy.onclick(speedy_clicked)

wn.mainloop()