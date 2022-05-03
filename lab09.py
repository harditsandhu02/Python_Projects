# CS 177 – lab09.py
# Hardit Sandhu
# This program will use the graphics and time library to create 
# a bouncing ball animation and will stop bouncing when clicked on.

from graphics import *
import time

# This function will create the window for the game and will 'return' it to be 
# used with other functions.
def createGameCanvas():
    # creating the window (name and size)
    win = GraphWin('Game Canvas',500,500)
    # setting a color to the canvas' background
    win.setBackground('brown')

    return win # returning the window to be used again

# This function will create the ball
def drawCircle(win):
    p = Point(250,470) # setting the starting location to the 'x' and 'y' variables
    # creating a circle with the previous points and setting the radius
    c = Circle(p, 30)
    # drawing the circle onto the window
    c.draw(win)
    # setting or 'filling' the color to blue
    c.setFill('blue')
    c.setOutline('black') # creating an outline

    return c # returning the ball to be used again

# This function will check if the 'click' from a mouse is inside the ball.
def checkForClickInsideCircle(win, circle):
    # setting the click to have a point
    pt = win.checkMouse()
    # if the click was not on the ball
    if not pt:
        return False # then the code will tell the rest of the program to not register it
    
    # getting the 'x' and 'y' points the mouse point/click
    mx,my = pt.getX(), pt.getY()
    # getting the center of the circle
    center = circle.getCenter()
    # getting the center points of the 'x' and 'y'
    cx,cy = center.getX(), center.getY()

    # calculating the distance
    dist = ((mx-cx)**2 + (my-cy)**2)**.5
    # returning true or false if the distance is less or greater than the circle's radius 
    return dist <= circle.getRadius() #if the click was inside the circle 

# This function will create the bouncing effect for the ball
def checkBoundary(circle, direction):
    # getting the center of the circle
    center = circle.getCenter()
    # getting the 'y' cord of the center
    Y = center.getY()
    # if the 'Y' is greater than the top of the window
    if Y >= 30:
        # the ball will move down
        direction = 1
    # if the 'Y' is greater than the bottom of the window
    if Y >= 470:
        # the ball will move up
        direction = -1
    
    return direction # returning the final direction so the 'play' function can use it
    
# This function will be the 'play' part of the program 
def play(window, circle, speed):
    direction = 0
    # The while loop keeps the ball moving up and down
    # until a click is detected inside the circle
    while True:
        # move the circle
        circle.move(0,speed)
        # pause the execution to observe the movement
        time.sleep(0.01)
        # determine the direction of the movement based on the speed
        if speed < 0:
            direction = -1
        else:
            direction = 1
        # changing the speed based on the direction
        speed = speed * checkBoundary(circle, direction)

        # the ball is clicked then it will stop moving
        if(checkForClickInsideCircle(window, circle)):
            break

# the main function where all the functions will be called
def main():
    # create a window
    window = createGameCanvas()

    # create a circle
    circle = drawCircle(window)
        
    #intial speed is negative (bottom to top)        
    speed = -2

    # call play to start the animation
    play(window, circle, speed)

    window.getMouse()
    window.close()
    
main()
