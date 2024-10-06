# Set exercise - printing set of cubic numbers and square numbers


def main():

    # x**3 represent cube no
    cubic_set = {x**3 for x in range(10)}
    print(cubic_set)

    # x**2 represent square no
    square_set = {x**2 for x in range(10)}
    print(square_set)

    # printing intersection

    print(cubic_set.intersection(square_set))

    # printing difference

    print(cubic_set.difference(square_set))


main()
