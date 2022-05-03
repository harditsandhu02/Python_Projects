# CS 177 – L09-Q2.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# Using conditional statemments, the user will input 3 values and the code
# will output the median


#-----MAIN-----

def main(): # creating a main variable where the code can be called from

    # the user will input three values for the function to run
    num1 = eval(input("​​Enter a number: "))
    num2 = eval(input("​​Enter a number: "))
    num3 = eval(input("​​Enter a number: "))
    
    # using multiple conditional statements the codw will print the median
    
    if((num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3)):
        print("median =",num1) # if the the first number is in the middle, print number 1
        
    # if not number 1
    elif((num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3)):
        print("median =",num2) # if the the second number is in the middle, print number 2
        
    # if not number 2
    elif((num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2)):
        print("median =",num3) # if the the third number is in the middle, print number 3

main()

