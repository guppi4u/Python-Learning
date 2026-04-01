# Creating calculator app 

def Calculator():
    number1 =int(input('Enter first number \n'))
    number2 =int(input('Enter second number \n'))

    def addition():
         add=(number1 + number2)
         return add
    def subtraction():
         sub=(number1 - number2)
         return sub
    def multiplication():
         mul=(number1 * number2)
         return mul
    def division():
         div=(number1 / number2)
         return div
    def modulo_divison():
         mod_div=number1 % number2
         return mod_div
    def floor_division():
         flr_div=number1 // number2 # this will just give whole number 
         return flr_div
    def exponential_calculation():
         exp_cal=number1 ** number2 
         return exp_cal
    
    print(f'Addition of 2 numbers {number1} and {number2} result is : {addition()}')
    print(f'Subtraction of 2 numbers {number1} and {number2} result is : {subtraction()}')
    print(f'Division of 2 numbers {number1} and {number2} result is : {division()}')
    print(f'Multiplication of 2 numbers {number1} and {number2} result is : {multiplication()}')
    print(f'Modulo division of 2 numbers {number1} and {number2} result is : {modulo_divison()}')
    print(f'Floor division of 2 numbers {number1} and {number2} result is : {floor_division()}')
    print(f'Exponentital of 2 numbers {number1} and {number2} result is : {exponential_calculation()}')

Calculator()