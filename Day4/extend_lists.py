# Program to extend lists

def main():
    numbers = ["one", "two", "three", "four", "five", "six", "seven"]
    print(type(numbers))
    print(numbers)
    print("*************************************************")

    print(numbers[3:7])
    print("*************************************************")

    # this is list with starting , ending index (included) and step
    numbers[3:7:2] = ["hello", "hi"]
    print(numbers)
    print("*************************************************")

    # printing with no starting or ending index , only steps count is given
    greeting = "Hello there"
    print(greeting[::2])

    print("What are you ?"[3::3])


main()
