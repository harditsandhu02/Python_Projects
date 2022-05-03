# CS 177 – lab06-Q1.py
# Hardit Sandhu
# Following Coding Standards and Guidelines
# The program will accept the user's two inputs (a 5-digit number and 
# a text) and output an encrypted text

# function where the key and encrytion is housed
def encrypt(number, text):

    # loop where the ASCII values for the text are computed
    ordC = 0 
    for i in str(number):
        ordC += ord(i) # adding the number together

    # loop where the number values are added together
    SumNumber = 0
    for i in str(number):
        SumNumber += int(i)

    key = ((ordC % SumNumber) + 50) # the key for the encrypt 
    lst = [] # list where the individual codes will be housed

    # the loop where the individual codes will be produced
    for i in text:
        en = chr((ord(i) + key) % 128)
        lst.append(en) # adding to the list

    # removing the list form of the combined code
    fencrypt = ''.join(str(x) for x in lst)

    return(key, fencrypt) # producing the key and code


# function where the code will be housed
def main():
    
    # asking the user for their number and text
    number = int(input("Please enter a 5-digits number: "))
    text = str(input("Please enter the text to be encrypted: "))

    print(encrypt(number, text)) # displaying the final product to the user

# calling the main function
if __name__ == "__main__": 
    main()