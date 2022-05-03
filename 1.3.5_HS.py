#%%

# Hardit Sandhu

#13
def how_eligible(essay):
    x = 0 # number of punctuation marks
    # if punctuation detected, add 1 to total punctuation
    if ('?' in essay): #?
        x += 1 
    if ('"' in essay): #!
        x += 1
    if ('.' in essay): #.
        x += 1
    if ('!' in essay): #,
        x += 1
    return x # returns the final number of punctuation marks


def slicer(phrase): 
    if (phrase == "I am a Patriot student, my school is awesome!"): #  if correct string
        return phrase[0:4] + phrase[36:45] # return the "sliced" string 
    else:
        print("You did something wrong!") # if it's an incorrect string, then it returns this


#%%