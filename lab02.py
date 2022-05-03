# CS 177 – lab02.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# This program accepts 2 values (height and weight) and outputs the Magic Number


# ----- Task #1 -----

print("This program calculates your 'Magic Number'")

name = input("What is your name?: ")
height = eval(input("How tall are you in meters?: "))
weight = eval(input("How x,much do you weigh in Kg?: "))

# ----- Task #2 -----

MK = ((height**5) + (weight**2))**(1/3)

# ----- Task #3 -----

print(name,", your magic number is: ", MK)
