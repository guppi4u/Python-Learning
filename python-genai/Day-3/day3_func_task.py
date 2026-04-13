# Wrinting a function to calculate area of rectangle 

def calculare_area_rect():
    '''Function to calculate area of rectangle'''
    length =float(input('Enter length of rectangle > '))
    width=float(input('Enter width of rectangle > '))
    return print(f'Area of rectangle : {length * width} m')


calculare_area_rect()


print("*" * 50)

def is_given_num_even():
    '''Function to calculate if user entered number is even'''
    user_input=int(input('Enter your number > '))

    if user_input%2==0:
        print('Number is even')
    else:
        print('Number is odd')

is_given_num_even()

print("*" * 50)

def get_score():
    '''Function to check grades based on score'''
    score=int(input('Enter your score > '))
    if score > 95:
        print('Grade A')
    elif score > 85 and score < 90:
        print('Grade B')
    elif score > 75 and score < 80:
        print('Grade C')
    elif score < 75:
        print('Grade D')

get_score()


def count_vowels():
    vowels=['a','e','i','o','u']
    vowels_count=0
    user_input=input('Enter your text > ')

    for i in user_input:
        if i in vowels:
            vowels_count +=1

    print(f'Number of vowles in user_input is : {vowels_count}')


count_vowels()

print("*" * 50)

        

