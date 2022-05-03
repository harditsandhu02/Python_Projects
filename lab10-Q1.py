# CS 177 – lab10-Q1.py
# Hardit Sandhu
# This program will take two stirngs and will output a list of 
# common letters sorted ascendingly

# this function will find the common letters between the two strings
def findCommonLetters(word1, word2):
    # initializing the list
    temp = []
    # first for loop to go through each letter in word # 1
    for i in range(len(word1)):
        # second for loop to go through each letter in word # 2
        for x in range(len(word2)):
            # checking if the letters mach
            if word1[i] == word2[x]:
                # if so, the program will add it to the temporary list
                temp.append(word1[i])

    # converting the list into a set so there will be no duplicates 
    new = set(temp)
    # outputting the set but sorted in 'abc' order
    return sorted(new)

# this function is used to test each input
def main():

    print(findCommonLetters('apple', 'party'))
    print(findCommonLetters('apple','apple'))
    print(findCommonLetters('watermelon', 'underwater'))
    print(findCommonLetters('', ''))
    print(findCommonLetters('','apple'))

# calling the main function
if __name__ == "__main__":
    main()