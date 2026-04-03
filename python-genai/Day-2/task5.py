
# Task 5: for Loop Practice

def loop_practice():
    count_even=0
    count_odd=0
    sum=0
    product=1
    for i in range(1,20):
        sum+=i
        product*=i
       
        if i%2==0:
            print(f'Even number :{i}')
            count_even+=1
            
        else:
            print(f'Odd number :{i}')
            count_odd+=1

    print(f'No of even number :{count_even}')
    print(f'No of odd number :{count_odd}')
    print(f'Sum of all the numbers :{sum}')
    print(f'Product of all the numbers :{product}')

    print("*************************************")

    for i,element in enumerate(range(1,20)):
        print()
        print(f'{element} is at index {i}')
        print()



loop_practice()       