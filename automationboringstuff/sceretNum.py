'''
Guessing secret number 
'''

import random
secret_number =random.randint(1,21)
print('I am an AI and thinking of number between 1 and 20')

# givinig user number of attempt 
for guesses_taken in range(7):
    print('Take guess')
    guess = int(input('>'))

    if guess < secret_number:
        print('Too low')

    elif guess > secret_number:
        print('Too high')
    else:
        break

if secret_number == guess:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))




