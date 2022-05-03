# CS 177 – L09-Q3.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# By importing the math library, the user will input 3 values and the code
# will output the the 3 angles of a triangle

# this code will import the math library to find the angle
import math 

#-----MAIN-----

def main(): # creating a main variable where the code can be called from

    # the user will input three values for the function to run
    a = eval(input("Enter length of side a: "))
    b = eval(input("Enter length of side b: "))
    c = eval(input("Enter length of side c: "))

    # by using the cosine formula, the code will export the side of each angle
    angleC = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
    angleB = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
    angleA = math.degrees(math.acos((c**2 + b**2 - a**2)/(2*c*b)))
    
    print("The angle between a and b is: ",angleC) # print angle C
    print("The angle between b and c is: ",angleA) # print angle A
    print("The angle between c and a is: ",angleB) # print angle B
    
    
main()


