#   a116_ladybug.py
import turtle as trtl
r = 180
c = 130
f = 50 

# create spider head and body
painter = trtl.Turtle()
painter.pensize(200)
painter.circle(25)
painter.pencolor("black")
painter.penup()
painter.goto(0, -c) 
painter.pendown()
painter.pensize(40)
painter.circle(20)
painter.penup()
painter.goto(0, -c) 
painter.pendown()
painter.pensize(5)
painter.pencolor("red")
painter.circle(7)
painter.penup()
painter.goto(15, -c) 
painter.pendown()
painter.pensize(5)
painter.pencolor("red")
painter.circle(7)
painter.penup()


# left legs of body 
painter.pencolor("black")
painter.goto(0,0) 
painter.setheading(75)
painter.pensize(10)
painter.pendown()
painter.circle(c,r)
painter.penup()
painter.goto(0,0) 
painter.setheading(100)
painter.pensize(10)
painter.pendown()
painter.circle(c,r)
painter.penup()
painter.goto(0,0) 
painter.setheading(125)
painter.pensize(10)
painter.pendown()
painter.circle(c,r)
painter.penup()
painter.goto(0,0) 
painter.setheading(150)
painter.pensize(10)
painter.pendown()
painter.circle(c,r)
painter.penup()

# right legs of body 
painter.goto(0,0) 
painter.setheading(100)
painter.pensize(10)
painter.pendown()
painter.circle(-c,r)
painter.penup()
painter.goto(0,0) 
painter.setheading(75)
painter.pensize(10)
painter.pendown()
painter.circle(-c,r)
painter.penup()
painter.goto(0,0) 
painter.setheading(50)
painter.pensize(10)
painter.pendown()
painter.circle(-c,r)
painter.penup()
painter.goto(0,0) 
painter.setheading(25)
painter.pensize(10)
painter.pendown()
painter.circle(-c,r)
painter.penup()
#a black widow hourglass shape
painter.pencolor("red")
painter.penup()
painter.goto(25,0) 
painter.setheading(r)
painter.pendown()
painter.forward(f)
painter.setheading(75)
painter.forward(f)
painter.setheading(125)
painter.forward(f)
painter.setheading(0)
painter.forward(f)
painter.setheading(245)
painter.forward(f)
painter.setheading(315)
painter.forward(f)

wn = trtl.Screen()
wn.mainloop()