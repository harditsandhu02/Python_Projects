# CS 177 lab4.py
# Hardit Sandhu 33539695
# This program prompts the user for the three weather
# attributes and decides whether or not a football
# should be canceled or not

def main():

    # prompt the user for the weather parameters
    print("Enter the weather attributes:")
    outlook = input("Outlook: ")
    humidity = input("Humidity: ")
    wind = input("Wind: ")
    

    # validate the input parameters
    a = False
    if(outlook == "Sunny"):
        a = True
    elif(outlook == "Overcast"):
        a = True
    elif(outlook == "Rain"):
        a = True

    # implement the solution using conditional structures
    # and print the outcome
    if( a == True):
        if(outlook == "Overcast"):
            print("Decision: Play")

        elif(outlook == "Sunny"):
            if(humidity == "High"):
                print("Decision: Cancel")
            elif(humidity == "Low"):
                print("Decision: Play")
    
        elif(outlook == "Rain"):
            if(wind == "Strong"):
                print("Decision: Cancel")
            elif(wind == "Weak"):
                print("Decision: Play")
    else:
        print("INVALID INPUT!")

main()
