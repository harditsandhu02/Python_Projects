#%%

# Hardit Sandhu

import matplotlib.pyplot as plt
import random

#10a
def roll_hundred_pair():
    # produces a histogram of the results of 100 rolls of two 6-sided dice
    a = []
    while len(a) < 100:
        a.append(random.randint(1,6) + random.randint(1,6))
    plt.hist(a)
    plt.show()
    
    
#10b
def dice(d):
    # returns the sum of a random roll of n 6-sided dice
    total = 0
    for x in range(0,d):
        total += random.randint(1,6) #select from range 1 - 6
    return total


#11a
def hangman_display(guessed, secret): # guessed : letters guessed so far 
    # secret : the full secret word or phrase
    letters = ''
    for b in secret:
        x = 0
        for a in guessed:
            if b.lower() in a .lower():
                x = 1
        if x == 1 or (b in ".,?'!"):
            letters += b
        else:
            letters += "-"
    return letters # returns the string a player would see
    
#11b
def matches(ticket,winners): # two lists 
    x = 0
    a = 0
    while x < len(ticket):
        if ticket[x] in winners:
            a += 1
        x+=1
    return a # returns an integer how many numbers the two lists have in common
# %%
