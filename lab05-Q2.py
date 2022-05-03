# CS 177 – lab05-Q2.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# The program will use numbers starting from 1 to 9 and display the ones
# that are special two-digit numbers (a number such that when the sum of the
# digits of the number is added to the product of its digits, the result is
# equal to the original two-digit number.



# The main function
def main():

    def special_digit():
        some = 0 # creating the variable for the sum and product values to be combined and housed
        
        lst = [] # making the list for the numbers to be housed in
        
        for i in range(1,10): # checking each number from the number range
            some = (i + 9) + (i * 9) 
            if ((int(some / 10) == i) and (some % 10 == 9)): # checking if has the same values as the two variables
                lst.append(some) # adding the correct number to the list

        lst.sort(reverse=True) # reversing the list to make it in decending order
        return(lst) # returning the final list so it can be displayed

    
    # Printing the result returned by special_digit
    print(special_digit())


# Calling main
main()

