# creating of complex array by metioning the dtype at creation time

import numpy as np


def main():
    values = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
    print(values)


main()
