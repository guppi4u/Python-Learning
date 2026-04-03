
# Task 5: for Loop Practice

def loop_practice():
    count_even=0
    count_odd=0
    for i in range(1,20):
        if i%2==0:
            print(f'Even number :{i}')
            count_even+i
            print(count_even)
        if i%2 ==1:
            print(f'Odd number :{i}')
            count_odd+i
            print(count_odd)




loop_practice()       