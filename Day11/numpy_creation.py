# program for creating numpy

import numpy as np


def main():

    # this is will create array of 15 element of shape 3 rows and 5 column
    newarray = np.arange(15).reshape(3, 5)

    print(newarray)

    # dtype
    print(f'dtype of array is : {newarray.dtype}')

    # item size

    print(f' item size of array is {newarray.itemsize}')

    # arrray type
    print(f'Type of array is :{type(newarray)}')


main()
