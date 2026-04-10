# Creating calculator with while loop 

def while_calculator_app():

    # creating user display 

    while True:
        print("\n========= Calculator =========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Divison")
        print("5. Exit")

        # Asking user to enter their choice 
        user_choice = input('Enter your choice >')
        
        # hadling first exist case 
        if user_choice == "5":
            print('Thank you !!!')
            break
        
        # selecting choice 
        if user_choice in ["1","2","3","4"]:
            # asking user to enter number 
            number_1 =float(input('Enter 1st number : '))
            number_2 =float(input('Enter 2nd number : '))
            result=0
            if user_choice =="1":
                result = number_1 + number_2
            elif user_choice =="2":
                result = number_1 - number_2
            elif user_choice =="3":
                result = number_1 * number_2
            elif user_choice =="4":
                if number_2 != 0:
                    result = number_1 / number_2    
                else:
                    print('Zero division , not possible')
                    continue

            print(f'Results : {result}')
            print()
        else:
            print('Invalid choice')

        
while_calculator_app()