# CS 177 – lab06-Q2.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# The program will accept the user's inputs (2 integer values)
# and output whether thoes values are coprime or not

# function where the GCD is housed
def GCD(num1, num2):
    zero = False
    remainder = 0 # the remainder 
    GCD = 0 # greatest common divisor

    # While loop to compute the factor
    while zero == False: 
        remainder = num1 % num2 # getting the remainder
        GCD = num2 # setting the remainder to GCD

        # if the remainder zero then the loop will end
        if(remainder == 0):
            zero = True
        
        # if the loop does not end, the num parameters will get new values
        else:
            num1 = num2
            num2 = remainder

    # returning the GCD 
    return GCD 

# function where the True or False is housed 
def coprime(num1, num2):
    # if statement to determine whether the integers are coprime or not
    if GCD(num1,num2)!= 1: 
        return False
    else:
        return True

def main(): # main function where the users input and output will be housed
    # asking the user for their values/parameters
    fInt = int(input("Please input the first integer: "))
    sInt = int(input("Please input the second integer: "))

    # displaying the output to the user
    print(coprime(fInt, sInt)) 

# calling the main function
if __name__ == "__main__": 
    main()