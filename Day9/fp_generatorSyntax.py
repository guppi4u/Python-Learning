# generator syntax


def main():

    # creating list of tuples
    result = print(list((x, y) for x in range(0, 4) for y in range(0, 4)))
    print(result)


main()
