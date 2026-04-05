
# Task 6: Combining Concepts

def task6_concepts():
    num_list=[] 

    # asking user to input 5 numbers 
    for i in range(5):
        user_input=int(input('Enter  five numbers >'))
        num_list.append(user_input)
        print()

    print(num_list)
    print()
    print(f'Lists max number is {max(num_list)}')
    print()
    print(f'Lists min number is {min(num_list)}')
    print()
    avg_list=sum(num_list)/len(num_list)
    print()
    print(f'Average list : {avg_list}')
    print()
    
    # creating dic to store result 
    results = {'high': [], 'medium': [], 'low': []}
    for i,item in enumerate(num_list):
        if item >=80:
            print(f'num {item} at position {i} is high\n')
            results['high'].append({'value': item, 'position': i})
        elif item >=50:
            print(f'num {item} at position {i} is medium\n')
            results['medium'].append({'value': item, 'position': i})
        elif item < 50:
            print(f'num {item} at position {i} is low\n')
            results['low'].append({'value': item, 'position': i})
    print(results)

                       
task6_concepts()