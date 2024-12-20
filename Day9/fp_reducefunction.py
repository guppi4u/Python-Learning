# program for reduce function

from functools import reduce
from operator import add


def main():
    numbers = [1, 2, 3, 4, 5]

    # this will reduce all the numbers by adding it

    print(reduce(lambda x, y: x+y, numbers))

    # same as above is done via operator

    print(reduce(add, numbers))


main()
