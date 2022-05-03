# CS 177 – lab08-Q1.py
# Hardit Sandhu
# This program will output a peace sign with the 
# provided directions using 'graphics.py']

# importing the graphics.py file to be able to use the attributes
from graphics import *

def drawPeaceSymbol():
    # creating a window and setting the background to the color black
    win = GraphWin('My window',500,500)
    win.setBackground('white')

    # first cricle to be the shown 'crescent'
    p = Point(250,250) # setting the location to 'x' and 'y'
    # creating a circle with the previous points and setting the radius
    c = Circle(p, 150)
    # drawing the circle in the win
    c.draw(win)
    # setting or 'filling' the color to black
    c.setFill('black')

    # setting the 'shade' of the crescent
    p2 = Point(250,250) # setting the location to 'x' and 'y'
    # creating a circle with the previous points and setting the radius
    c2 = Circle(p2, 149)
    # drawing the circle in the win
    c2.draw(win)
    # setting or 'filling' the color to white
    c2.setFill('white')

    # creating the middle line for the peace sign
    MLine = Line(Point(250,100), Point(250,400))
    MLine.draw(win)

    # creating the right line for the peace sign
    rp = Point(250,250)
    rline = Line(rp, Point(335, 374))
    rline.draw(win)
    
    # creating the left line for the peace sign
    Lp = Point(250,250)
    Lline = Line(rp, Point(160, 371))
    Lline.draw(win)

    # being able to close the window with a mouse click
    win.getMouse()
    win.close()

# the main function where the other functions can be called
def main():
    # calling the 'drawPeaceSymbol' function
    window = drawPeaceSymbol()

# calling the 'main' function
main()