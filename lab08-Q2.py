# CS 177 – lab08-Q2.py
# Hardit Sandhu
# This program will output the Aaptian Amercia sheild with the 
# provided directions using 'graphics.py']

# importing the graphics.py file to be able to use the attributes
from graphics import *

def drawShield():
    # creating a window and setting the background to the color 'black'
    win = GraphWin("Captain America's Shield",500,500)
    win.setBackground('White')

    # first cricle to be the shown as the first layer as the sheild
    p = Point(250,250) # setting the location to 'x' and 'y'
    #  creating a circle with the previous points and setting the radius
    c = Circle(p, 230)
    # drawing the circle in the win
    c.draw(win)
    # setting or 'filling' the color to red
    c.setOutline('black') # creating an outline
    c.setFill('red')

    # setting the second layer of the sheild
    p2 = Point(250,250) # setting the location to 'x' and 'y'
    # creating a circle with the previous points and setting the radius
    c2 = Circle(p2, 200)
    # drawing the circle in the win
    c2.draw(win)
    # setting or 'filling' the color to 'black'
    c2.setOutline('black') # creating an outline
    c2.setFill('white')

    # setting the third layer of the sheild
    p3 = Point(250,250) # setting the location to 'x' and 'y'
    # creating a circle with the previous points and setting the radius
    c3 = Circle(p3, 170)
    # drawing the circle in the win
    c3.draw(win)
    # setting or 'filling' the color to red
    c3.setOutline('black') # creating an outline
    c3.setFill('red')

    # setting the fourth layer of the sheild
    p3 = Point(250,250) # setting the location to 'x' and 'y'
    # creating a circle with the previous points and setting the radius
    c3 = Circle(p3, 140)
    # drawing the circle in the win
    c3.draw(win)
    # setting or 'filling' the color to blue
    c.setOutline('black') # creating an outline
    c3.setFill('blue')

    # being able to close the window with a mouse click
    win.getMouse()
    win.close()

# the main function where the other functions can be called
def main():
    # calling the 'drawsheild' function
    window = drawShield()
    
# calling the 'main' function
main()