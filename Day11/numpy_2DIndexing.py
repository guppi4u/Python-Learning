# program for 2D indexing


import numpy as np


def main():
    num = np.arange(16).reshape(4, 4)

    print(num)
    print()

    # selecting 1st subarray

    print(num[0])
    print()

    print(num[0, :])
    print()

    # printing 1st column
    print(num[:, 0])


main()
