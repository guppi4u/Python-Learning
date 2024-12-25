# Program for numpy


import numpy as np


def main():
    num1 = np.array([1, 2, 3, 4, 5, 6], dtype='int')
    num2 = np.array([1, 2, 3, 4, 5, 6], dtype='float')

    print(num1)

    # data type of data
    print(num1.dtype)

    # dimention dimention of
    print(num1.ndim)

    # shape of data
    print(num1.shape)

    print(num2)

    print("**************************")

    # 2D array

    num3 = np.array([[1, 2], [3, 4], [5, 6]])
    print(num3)
    print(num3.ndim)
    print(num3.shape)


main()
