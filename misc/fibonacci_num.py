# Creating a program for calculating fibonacci numbers 

def fibonacci_num(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    
    # creating ele1 and ele2 , sum variables 
    # To calculate the 3rd number, we need the 1st and 2nd numbers. elem_1 and elem_2 are initialized to 1
    elem_1 = elem_2 = 1

    # initalizing sum to 0 
    the_sum=0

    # calculating sum through for loop 
    for i in range(3,n+1):
        # now sum is e1em_1 + elem_2
        the_sum = elem_1 + elem_2
        # replacing elem_2 by the_sum for next iteration 
        elem_1, elem_2 = elem_2,the_sum
    return the_sum

# checking the function  
for n in range(1,10):
    print(n,"->",fibonacci_num(n))
