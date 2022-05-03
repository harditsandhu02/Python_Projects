# CS 177 – lab05-Q1.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# The program will use numbers starting from 1869 to 2020 and display the ones
# that are are divisible by 7 and multiple of 5



# The main function
def main():


    # creating the question function     
    def findNumbers():
        
        lst = [] # making the list for the numbers to be housed in
        
        for i in range(1869, 2021): # checking each number from the number range
            if (i % 7 == 0 and i % 5 == 0): # checking if divisible by 7 and multiple of 5
                lst.append(i) # adding the correct number to the list
                
        return(lst) # returning the final list so it can be displayed
        

    

    # Printing the result returned by findNumbers
    print(findNumbers())


# Calling main
main()
