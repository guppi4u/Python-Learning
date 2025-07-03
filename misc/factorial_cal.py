# Creating a program to calculate factorial of numbers 

def factorial_cal(n):
    if n < 0:
        return False
    if n < 2:
        return 1
    
# decalring a variable called 'product' which takes 1 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

 # testing of function    
for n in range(1,6):
    print(n,factorial_cal(n))