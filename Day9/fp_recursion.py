# recursion program -function calling itself


def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)


def main():

    print(factorial(5))
    print(factorial(6))


main()
