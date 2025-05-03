''' 
creating list comprehensions
'''

def Listcomprehensions():

    squares = [x ** 2 for x in range(10)] # squares

    print(f'Values of squares list :{squares}')

    twos = [2 ** i for i in range(8)] # twos

    print(f'Values of twos :{twos}')

    odds = [x for x in squares if x % 2 != 0 ] # odds 

    print(f'Values of odds list: {odds}')







def main():
    Listcomprehensions()


main()