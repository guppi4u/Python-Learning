# program for advance indexing

import numpy as np


def main():

    num = np.arange(16).reshape(4, 4)

    print(num)
    print()

    # where [1,2,3]- is row & [0,1,3] is column
    values = num[[1, 2, 3], [0, 1, 3]]

    print(values)
    print("************")

    # can also pass conditions

    print(num[num % 2 == 0])
    print("************")

    print(num[num < 5])


main()
