# CS 177 – lab10.py
# Hardit Sandhu
# This program will utilize the 'speech.txt' file to read from it and 
# will output a dictionary with the most common 'words'

import string # importing the string file so it can be used in the program


# this function will read from the text file and ouput two lists
def readParagraphs(filename):
    # initializing the two lists
    final = []
    secfinal = []
    # opening the file
    infile = open(filename, 'r')

    # counting amount of lines in the file 
    with open(filename) as filef:
        line_count = 0
        # for each line, the total amount will go up by one
        for line in filef:
            line_count += 1

    # this for loop will go through the file 
    for i in range(line_count):
        # reading the line
        speech = infile.readline()
        # removing punctuation to 'clean' up the text
        cleanSpeech = speech.translate(str.maketrans('', '', string.punctuation))
        # if the text is the second paragraph
        if i == line_count-1:
            # add the text to the list
            secfinal.append(cleanSpeech.lower())
        # if it is the first paragraph
        else:
            # add the text to the list
            final.append(cleanSpeech.lower())

    # retuing the two lists to be used by other functions
    return (final[0].split()),(secfinal[0].split())

# this function will find the similar words between each list and will find how many times they were in the list
def similarityAnalysis(paragraph1, paragraph2):
    # converting the lists into sets
    unique_words1 = set(paragraph1)
    unique_words2 = set(paragraph2)
    
    # creating a empty dictionary
    words_dict1 = {}
    # first for loop to go through list 1
    for word in unique_words1:
        # first for loop to go through list 2
        for word2 in unique_words2:
            # if the words match
            if word == word2:
                # create a list with the amount in each list
                new = [paragraph1.count(word),paragraph2.count(word2)]
                # adding the values to the dictionary with a key
                words_dict1[word] = new

    # retuing the set to be used by other functions
    return(words_dict1)

# main function to call the functions
def main():
    par1, par2 = readParagraphs('speech.txt')
    print(par1)
    print(par2)

    print(similarityAnalysis(par1, par2))

# calling the main function
if __name__ == "__main__":
    main()