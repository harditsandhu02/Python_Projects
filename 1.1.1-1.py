import turtle as trtl

q = trtl.Turtle() # initializing q
h = 100 # initializing h

# creating the head and neck
q.pensize(3)
q.penup()
q.goto(-100,-10)
q.pendown()
q.setheading(h - 10)
q.forward(50)
q.right(h-10)
q.forward(50)
q.circle(h)
q.forward(50)
q.right(h-10)
q.forward(50)

# creating the mouth
q.penup()
q.goto(0,h)
q.pendown()
q.setheading(h + 80)
q.forward(h)
q.penup()
q.setheading(h - 10)
q.forward(70)

# creating the left eye 
q.pendown()
q.circle(-10)
q.setheading(0)
q.penup()
q.forward(h)

# creating the right eye
q.setheading(h - 10)
q.pendown()
q.circle(10)

wn = trtl.Screen()
wn.mainloop()
