# passing one functions to another

# this will double the value which is passed
def double(n):
    return n * 2


def apply(values, f):

    # creating an empty list
    result = []

    for value in values:
        result.append(f(value))

    return result


def main():
    numbers = [2, 4, 6, 8, 10]

    result = apply(numbers, double)

    print(result)


main()
