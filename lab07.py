# CS 177 – lab07.py
# Hardit Sandhu
# This code will read from the "companies.txt" file and output the
# average of investments each company made and will stop once a negative
# number was encountered.

# function where the code will read from the '.txt' file and 
# add the contents to a list
def readCompaniesData(filename):

    # creating the list and opening the file
    greater = [] # empty list where the text will be added to 
    infile = open(filename, 'r') # opening the file so the code can start to read from it 

    # simple for loop to 'get' the data from the file and add them to the list one by one
    for line in infile.readlines():
        # creating a list from each line
        data = line.strip().split(',') # striping the txt from the '\n' and ','
        greater.append(data) # adding the data to a list 

    return(greater) # outputting the list for the other funtion to use


# funtion where the code will compute the average amount of investments. 
# However, will stop computing once/if it reaches a negative number
def computeAverageInvestment(investmentData):

    sort = sorted(investmentData, key=lambda x: x[0]) # sorting the list in 'abc' order

    # first for loop to access the main list 
    for i in sort:
        total = 0 # creating the total where each value will be added to 
        count = 0 # creating a value where the number of values will be added to 
        # nested or second for loop to access the sublist
        for x in i:
            if x.isalpha(): # if a object is a string (word) then it will be saved
                name = x # storing the word
            elif eval(x) > 0: # if not and if the value is greater than '1'
                total = total + eval(x) # add the value to the total 
                count = count + 1 # increasing the count by 1 or each value added
            else: # if the value is a negative number, then the loop will stop
                break # stopping the loop 

        ave = total/count # computing the average of each sublisgt
        i.clear() # clearing the sublist to start with a fresh one
        i.append(name) # adding the word to give the sublist a 'name'
        i.append(ave) # lastly adding the average to the sublist

    return(sort) # returning the value so it can be stored

# main funtion where the other funtions can be called
def main():

    # calling readCompaniesData with a '.txt' file 
    companyInvestmentList = readCompaniesData('companies.txt')
    print(companyInvestmentList) # displaying the info 

    # calling computeAverageInvestment to get the average for each company
    averagesList = computeAverageInvestment(companyInvestmentList)
    print(averagesList)

#calling the main funtion
main()
