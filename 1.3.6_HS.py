#%%  
# Hardit Sandhu
import random

#15
def roll_two_dice(): # combines random rolls from two dice and prints
    return(random.randint(1,6) + random.randint(1,6)) 

#16 
def guess_letter(): # grabs a random letter from the alphabet
    j ="abcdefghijklmnopqrstuvwxyz" 
    return(j[random.randint(0,26)]) # returns that letter 
#%%

