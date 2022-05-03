#%%
# Hardit Sandhu 133

#6b, if-else
def report_grade (percent):
    '''Step 6b if-else'''
    if percent >= 80: # A grade equal or above an 80 is mastery in this class
        print ('A grade of', percent , 'percent indicates mastery.') # reports mastery if the argument percent is 80 or more.
    else:
        print ('A grade of' , percent , 'does not indicate mastery.') # if grade is below an 80, then the "else" it output'ed
    
            
#8, True/False Return
def letter_in_word (guess, word):
    if  guess in word: # returns True if guess is a letter in word 
        return True
    else:
        return False # returns False if the letter is not in the word 
        
#9, Hints
def hint (color, secret): # The function should print a hint telling whether the color is in string.
    if color in secret:
        print ("The color", color, "IS in the secret sequence of colors.") # if in string
    else:
        print ("The color", color, "IS NOT in the secret sequence of colors.") # if not in string
    
#%%