# CS 177 – L09-Q1.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# Using a for loop and an if statement, the code will output an int variable
# by continuously adding a number multiplied by 2


#-----MAIN-----

def main(): # creating a main variable where the code can be called from
    
    pennies = .01 # the value of a penny (to start with - day 1)
    final = 0 # initalizing the the final product varible

    # for loop constanly adding to the final count (for the 30 days)
    for i in range(30): 
        final = final + pennies # addinging 
        pennies = pennies * 2 # multiplying the penny count by 2 each iteration

    # printing the final count and evauating if it is greater
    # than the Uncle's amount
    print("Your father is giving you",final)

    # print an answer comparing it to the uncle's amount 
    if final > 1000000:
        print("GREATER") # if greater
    else:
        print("LESS") # if smaller
        
main()
