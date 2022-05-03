# CS 177 – lab10-Q2.py
# Hardit Sandhu
# This program will used a inputed list to output a simlar list
# but without any duplicate adjacent numbers

def removeAdjacentNumbers(numList):
    # while loop to have more control 
    # initializing variable i 
    i = 1
    while i < len(numList): # the list will continue as long as it's not outside the list's boundary
        # if two values are the same
        if numList[i] == numList[i-1]:
            # if so, the program will remove the value in the spot
            numList.pop(i)
            # setting the i value back one so the list can continue properly
            i = i - 1
        # increasing the i value to contine in the loop
        i = i + 1

    # outputting the list
    return numList

# this function is used to test each input
def main():
    print(removeAdjacentNumbers([1,2,3,4,5]))
    print(removeAdjacentNumbers([1,2,2,3,4,5,5]))
    print(removeAdjacentNumbers([]))
    print(removeAdjacentNumbers([1,2,3,1,2,3]))
    print(removeAdjacentNumbers([2, 2, 4, 4, 2, 2, 5, 5]))

# calling the main function
if __name__ == "__main__":
    main()