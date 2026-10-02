
"""
Write a program that simulates rolling one or more dice. Each time the program runs,
it should randomly generate numbers between 1 and 6 (inclusive) for each die,
display the results, and ask if the user would like to roll again.
"""

import os
from platform import system
import random


def dice_roller():
    '''This function simulates rolling a chosen number of dice and keeps rolling until the user decides to stop.'''

    while True:
        try:
            user_input = input("How many dice would you like to roll? (1-6): ")
        except EOFError:
            print("\nInput closed. Exiting dice roller.")
            return

        try:
            num_dice = int(user_input)
        except ValueError:
            print("Please enter a valid number between 1 and 6.")
            continue

        if num_dice < 1 or num_dice > 6:
            print("Please enter a number between 1 and 6.")
            continue

        break

    while True:
        dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
        print(f"Rolled values: {dice_rolls}")

        try:
            user_input = input("Would you like to roll again? (y/n): ").strip().lower()
        except EOFError:
            print("\nThank you for playing!")
            break

        if user_input == 'n':
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    # clear the console screen
    if system() == "Windows":
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    print("Welcome to the Dice Roller!")
    dice_roller()

