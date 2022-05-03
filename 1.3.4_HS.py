#%%
import random

def guess_once():
    secret = random.randint(1, 4) # the secret number 1 to 4
    print('I have a number between 1 and 4.')  
    guess = int(input('Guess: ')) # User input
    if guess != secret:
      if guess < secret:
        print('Too low, my number is ', secret, '.', sep='') # guessed too low
      else:
        print('Too high, my number is ', secret, '.', sep='') # guessed too high
    else:
        print('Correct!, my number is', guess, end='!\n') # Correct


#8, low/high quiz 
def quiz_decimal(low, high): # asks the user for a number between low and high and tells them whether they succeeded.
   print('Type a number between', low, 'and', high)
   chosen = float(input())
   if chosen < low: # if the input value is low 
     print('No,', chosen, 'is less than', low) 
   if chosen > high: # if the input value is high 
     print('No,', chosen, 'is greater than', high)
   else:
     print('Good!', low, '<', chosen, '<', high) # if the input value is low 
    
#%%
