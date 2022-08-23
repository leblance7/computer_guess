#Computerguess a number between 1 and 100

import random

DEBUG_MODE = True
    

def debug(*args):
    if DEBUG_MODE:
        print(f'=== DEBUG: {args} ===')
    
print("Pick a number between 1 and 100 but don't tell me!")
input('press enter when ready')

guess = random.randint(1, 100)
upper_bound = 100
lower_bound = 1

print(guess)
print('Is this your number?')

while True:
    #part 1
    input_value = input('Respond with too low (L), too high (H), or equal (E)')
    #part 2
    input_value.lower()
    #part 3
    input_value = input_value.lower()
    if input_value in ['h','too high']:
        upper_bound = guess -1 
        debug(upper_bound, 'UB')
        debug(lower_bound, 'LB')
        debug(guess , 'old guess')
        guess = random.randint(lower_bound, upper_bound)
        print(guess)
        print('Is this your number?')
    elif input_value in ['l','too low']:
        lower_bound = guess + 1
        debug( upper_bound, 'UB')
        debug( lower_bound, 'LB')
        debug(guess, 'old guess')
        guess = random.randint(lower_bound, upper_bound)
        print(guess)
        print('Is this your number?')
    elif input_value in ['equal', 'e']:
        print ('yes!')
  
    
    
    
