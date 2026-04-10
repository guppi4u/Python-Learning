
# 1 code 
def while_loop101():    
    count=0
    while count < 5:
            print(f'Value of count in this iteration is : {count}')
            count+=1
    print("************************")

def user_input_validation():
    # User input validation 
    while True:
        user_input=input('Enter your age > ')
        if user_input.isdigit() and int(user_input) <= 120:
            print('You are an Human !!!')
            break
    print('You are not an Alien!!!!')

print("***********************************")

def process_condition():
# Processing until condition met :
    total = 0
    while total < 100:
            num =int(input('Enter a number >'))
            total += num
            print(f'Running total : {total}')

print("***********************************")

while_loop101()
user_input_validation()
process_condition()

