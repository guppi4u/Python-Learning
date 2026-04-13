
# Random number guess by user 
# Using random module to guess number 


import random

def random_guess():
    '''Random number guess function'''
    attempt_count = 0 # this should always be outside while loop , else it will initialize to 0 each time while loop runs 
    random_number =random.randint(1,100) # for above same reason moving outside while loop 

    while True:
        try:
            # User input
            user_input =int(input('Enter your number (1-100) > '))
            if user_input > random_number:
                print('Too High!!!')
                attempt_count+=1
            elif user_input < random_number:
                print('Too low !!!')
                attempt_count+=1
            elif user_input == random_number:
                print('Bingo , you got the number !!!')
                print(f'Random number is: {random_number}, Number of Attempt by user : {attempt_count}')
                break
        except ValueError:
            # Catches non-numeric input (letters, special chars, etc.)
            print('Invalid input! Please enter only numbers (1-100).')
            continue    



random_guess()