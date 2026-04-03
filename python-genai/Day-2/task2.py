
# Task 2 --List operations


def list_operations_task():
    my_list = []
    
    while True:
        user_input = input('Enter your item :')
        
        # Exit condition FIRST
        if user_input == 'done':
            break
        
        # Then add to list
        if user_input not in my_list:
            my_list.append(user_input)
            print(f'{my_list}')
            # my_list.sort()
    
    print(f'Final list: {my_list}')

# Test
list_operations_task()
