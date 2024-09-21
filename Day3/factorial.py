# program for factorial in recursive manner


def calculate_factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n*calculate_factorial(n-1))


def main():
    userInput = int(input("Enter number :"))
    result = calculate_factorial(userInput)
    print(result)


main()
