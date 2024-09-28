# Program for functions in tuple


def main():
    numbers = 1, 2, 3, 3, 4, 7, 9, 9

    # printing length of tuple
    print(len(numbers))
    print("*****************")
    # printing max element in tuple
    print(max(numbers))
    print("*****************")

    # printing min element in tuple
    print(min(numbers))
    print("*****************")

    # counting number of elements in tuple
    print(numbers.count(9))


main()
