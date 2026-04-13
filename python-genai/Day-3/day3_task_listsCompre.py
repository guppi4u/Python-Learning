# List Comprehensions 

def learning_lists():

    spam=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # list of squares 

    squares=[n * n for n in spam ]

    print(f'Squared list of spam :{squares}')

    print("*" * 60)

    # even list 
    even_numbers =[n for n in spam if n % 2 ==0]

    print(f'Even numbers : {even_numbers}')

    print("*" * 60)

    # A list of numbers greater than 5, each multiplied by 2

    num_greater_than_five =[n * 2 for n in spam if n >5]

    print(f'Number in list greater than 5 and multipled by 2 : {num_greater_than_five}')

    print("*" * 60)
   
   # list of string 

    string_list =[str(x) for x in range(10)]

    print(f'List of strings : {string_list}')
   
    print("*" * 60) 

    # creating list of tuples (number square)

    number_square=[(x,x**2) for x in range(10)]

    print(f'Numbered suared tuples :{number_square}')
    print("*" * 60) 

learning_lists()