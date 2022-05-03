# CS 177 lab3.py
# Hardit Sandhu 33539695
# This program prompts the user for the number of terms and
# compute the pi approximation. Moreover, the program computes
# the absolute value of the difference between the calculated
# and math.pi


#----- TODO #2 -----

def main():
    import math
    
    divisor = 1
    Pi = 0
    x = 1

#----- TODO #3 -----
    
    # prompt the user for the number of iterations
    n = eval(input("Enter the number of iterations : "))
    
    # set up a variable before the loop to accumulate the result of the # computation
    divisor = 1
    Pi = 0
    x = 1

    # loop for n iterations
    for i in range(n):
        if x > 0:
            Pi = Pi + 4/divisor
            divisor = divisor + 2
            x = -1
        elif x < 0:
            Pi = Pi - 4/divisor
            divisor = divisor + 2
            x = 1

    # implement the solution
    MA = math.pi
    Dif = abs(MA - Pi)

    # print the approximation of pi
    print("The approximation of pi =",Pi)
    
    # print the absolute difference between math.pi and the computed pi
    print("The absolute difference  =",Dif)

main()
