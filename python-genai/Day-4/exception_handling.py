
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    
def get_number_from_user():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

num1 = get_number_from_user()
num2 = get_number_from_user()
division_result = safe_divide(num1, num2)
print(f"The result of dividing {num1} by {num2} is: {division_result}")
