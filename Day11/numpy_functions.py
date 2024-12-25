

import numpy as np


def main():
    num = np.arange(12).reshape(3, 4)

    print(num)
    print("****************************")

    # this will add all the column(axis=0)
    print(num.sum(axis=0))

    print("****************************")
    # this will add all the row(axis=1)
    print(num.sum(axis=1))


main()
