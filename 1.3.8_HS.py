#%%

# Hardit Sandhu

def goGuess():
    amountofG = 0
    guess = (int(input('Guess a number from 1 to 20')))
    actualG = random.randint(1,20)

    while guess != actualG:
        amountofG += 1
        if guess < actualG:
            print str(guess) + " is too low"
        else:
            print str(guess) + " is too high"
        
        guess = (int(raw_input('Guess a number from 1 to 20')))
    
    print 'Correct! My number is' + str(G) + 'You guessed it in' + str(amountofG) + 'amountofG!'

goGuess():


# gather start and end value from user
start = input("Start value: ")
end = input("End value: ")

def fizzbuzz(x):
    """ The FizzBuzz algorithm applied to any value x """
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

# apply fizzbuzz function to all values in the range
for x in map(fizzbuzz, range(start,end+1)):
    print "{0:>8s}".format(x)


# %%


