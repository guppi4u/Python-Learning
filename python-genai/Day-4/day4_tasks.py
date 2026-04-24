
# Task-1 Working with modules and packages

import math
import random
import datetime

from arrow import now

def math_modules():
    print("Square root of 144:", math.sqrt(144))
    print("Area of circle with radius 5:", math.pi * (5 ** 2))
    print("Factorial of 5:", math.factorial(5))

def random_modules():
    print('Generate a random 5 integer between 1 and 100:', [random.randint(1, 100) for _ in range(5)])
    print('Pick random color from list:', random.choice(['red', 'blue', 'green', 'yellow']))
    print('Shuffle a list of numbers:', random.sample(range(1, 11), 10))


def datetime_modules():
    now = datetime.datetime.now()
    print("Current date and time:", now)
    print("Seven days from now:", now + datetime.timedelta(days=7))
    print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))


math_modules()

print("*" * 20)
random_modules()

print("*" * 20)
datetime_modules()

print("*" * 20)

# Task-2 Exceptions and error handling

def divide_numbers():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        division_result = a / b
        print("The result of the division is:", division_result)
        additional_result = a + b
        print("The result of the addition is:", additional_result)
        subtraction_result = a - b
        print("The result of the subtraction is:", subtraction_result)
        multiplication_result = a * b
        print("The result of the multiplication is:", multiplication_result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")

divide_numbers()


# Task-3 Working with files

def file_operations():
    # asking user for file name
    file_name = input("Enter the name of the file to create: ")

    # try to open the file for reading, if it doesn't exist, create it and write some content
    try:
        with open(file_name, "r",encoding="utf-8") as file:
            print("File already exists. Content:")
            print(file.read())
    except FileNotFoundError:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("This is a sample file created for demonstration purposes.")
        print(f"File '{file_name}' created successfully.")
    except PermissionError:
        print("Error: You do not have permission to create or read this file.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    finally:
        print("File operation completed.")

file_operations()

print("*" * 20)


# Task-4 Working with APIs

import requests
def fetch_data_from_api():
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        print("Data fetched from API:")
        print(data)
        # parse and print specific fields from the data
        print("Title:", data.get("title"))
        print("Body:", data.get("body"))
        # extracting userId and making another API call to get user details
        user_id = data.get("userId")
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        print("User Name:", user_data.get("name"))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")


fetch_data_from_api()
