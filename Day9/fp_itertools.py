# program for iterator tools

import itertools as it


def main():
    items = it.product(range(-1, 2), range(-1, 2))

    # this will filter values like 0,0
    items = it.filterfalse(lambda v: v[0] == 0 and v[1] == 0, items)

    for x, y in items:
        print(x, y)


main()
