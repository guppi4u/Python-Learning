
"""

CLI-Calculator
"""

def calculator():
    print("==== CLI CALCULATOR===")
    print("Operator for calculation +,-,*,/")
    print(" Type exit to quit \n")

    while True:
        user_operators =input("Enter operator (+,-,*,/) or quit to exit:\n").strip().lower()

        if user_operators =='exit':
            print('Thank you !!!')
            break
        if user_operators not in ('+','-','/','*'):
            print('Invalid operators Try again!!!')
            continue

        try:
            num1 = int(input('Enter your first number:' ))
            num2 = int(input('Enter your second number:' ))
        except ValueError:
            print("Invalid number , Try again \n")
            continue

        if user_operators =="+":
            result = num1 + num2
        elif user_operators =="-":
            result = num1 - num2
        elif user_operators =="*":
            result = num1 * num2
        else:
            if num2 < 0:
                print('Error: Divide by zero !!!')
                continue
            result =num1 /num2
        print(f'Result : {result}')

if __name__ =="__main__":
    calculator()