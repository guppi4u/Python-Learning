
# importig specific functions from a module

from datetime import datetime, timedelta
from math import sqrt, pow
from random import choice,shuffle

# Using the imported functions
# Note: We cannot use math.sqrt or random.choice directly since we imported only specific functions.
print("Square root of 16 is:", sqrt(16))
print("2 raised to the power of 3 is:", pow(2, 3))
print("**" * 20)  # Just a separator for better readability

# Using functions from the random module
print("Random choice from a list:", choice(['apple', 'banana', 'cherry']))
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print("Shuffled list:", my_list)
print("**" * 20)  # Just a separator for better readability

# Using functions from the datetime module

print("Current date and time:",datetime.now())
print("**" * 20)  # Just a separator for better readability
print("Current year:", datetime.now().year)
print("Current month:", datetime.now().month)
print("Current day:", datetime.now().day)
print('Tomorrow\'s date:', datetime.now().date() + timedelta(days=1))
