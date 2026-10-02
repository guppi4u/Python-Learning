""" 

Number guessing game 
Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low.

"""

import random

def number_guessing_game():

    '''This function implements a number guessing game where the user tries to guess a randomly selected number between 1 and 100.'''

    secret_num =random.randint(1,50) # decalring var secret_num which hold secret number
    guess_count = 0 # initialzing var guess count 

    while True:
        guess_count += 1
        user_input = int(input('Guess secret number between 1 to 50 !!!'))

        if user_input < secret_num:
            print('Try again , Too low !!!')
        elif user_input > secret_num:
            print('Try again , Too high !!!')

        else:
            print("Congratulation you found it !!!!")
            print()
            print(f'Number of guesses you have taken is : {guess_count}')
            break




if __name__ == "__main__":
    number_guessing_game()