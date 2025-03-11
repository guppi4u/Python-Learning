# Prompt the user to enter a word
user_input = input("Enter your word\n")

# Assign it to the user_word variable and convert it to uppercase.
user_word = user_input.upper()

for letter in user_word:
    # Check if the letter is a vowel
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    # Print the letter if it's not a vowel
    print(letter)
