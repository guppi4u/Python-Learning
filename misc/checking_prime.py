'''
Function to check prime number
'''


def checking_prime(num):
    #This will loop from given num till squareroot of number
    for i in range(2,int(1+num**0.5)):
        if num % i ==0:
            print(f"{num}:-> Num is not prime")
            return False
        else:
            print(f"{num}:-> Num is prime")
            return True
            

checking_prime(8)