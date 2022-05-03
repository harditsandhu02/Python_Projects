# CS 177 – lab05-Q3.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# The program will ask the user for a word and the code will swap each
# character's case and will comvert each character to a numerical value

import string
# The main function
def main():

    # Prompt the user to enter a string
    secret = input("Enter a string: ")

    lst = [] # creating a list to store the variables
    
    def encode(x):
        
        w = x.swapcase() # swaping the characters' cases

        # a for loop to encode the characters
        for i in w: 
            wjd = ord(i)
            lst.append(wjd) # adding to list

        
        
        return(''.join(str(x) for x in lst)) # finally concatenating the list

        

    # Printing the result returned by encode
    print(encode(secret))


# Calling main
main()


