#creating guessing no game -LAB

# creating a secret number variable 
secret_number =777

print('*****WELCOME TO GAME OF GUESSING NUMBER*****')

#asking user input
user_input=int(input('Enter your number:\n'))

# using while loop for checking condition
while user_input != secret_number:

    print('Ha ha you are in my loop now!!!')
    
    # when while loop is true , asking user again for input
    user_input=int(input('Enter your number:\n'))
    
    # cheking again for condition
    if user_input == secret_number:

        print ('Thank god you got it')
# finally exit
print('Done!!!')

    


