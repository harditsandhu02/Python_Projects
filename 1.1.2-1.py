#%%
import turtle as trtl

#initializing the object
Y = trtl.Turtle()
Y.pensize(5)
Y.penup()

# asking the basic questions
user_name = input("What is your name?")
print("Hey!", user_name)
yno = input( "Would you like to help me with my program.") 

if yno == 'yes': # if the user says "yes"

    # making the first tire
    Y.goto(-50,0)
    Y.pendown()
    fav_tire = input("What color do you want the tire to be?")
    Y.begin_fill()
    Y.fillcolor(fav_tire)
    Y.circle(40)
    Y.end_fill()
    Y.penup()

    # making the front side of the car
    Y.setheading(165)
    Y.forward(80)
    Y.setheading(90)
    Y.pendown()
    Y.forward(35)
    Y.circle(-75, 135)
    Y.setheading(0)
    Y.forward(50)
    Y.setheading(90)

    # making the sitting area of the car
    fav_color = input("Whats your favorite color?")
    Y.fillcolor(fav_color)
    Y.begin_fill()
    Y.setheading(90)
    Y.forward(90)
    Y.setheading(0)
    Y.forward(100)
    Y.setheading(270)
    Y.forward(90)
    Y.end_fill()

    # making the backside of the car
    Y.setheading(0)
    Y.forward(35)
    Y.setheading(45)
    Y.circle(-75, 135)
    Y.forward(35)
    Y.penup()

    # making the back tire
    Y.setheading(180)
    Y.forward(80)
    Y.setheading(270)
    Y.forward(10)
    Y.setheading(180)
    Y.pendown()
    Y.begin_fill()
    Y.fillcolor(fav_tire)
    Y.circle(-40)
    Y.end_fill()

# a lovely message
print ("Have a great day!")

#end of code


wn = trtl.Screen()
wn.mainloop()
#%%