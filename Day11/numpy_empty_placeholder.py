# creation of empty array or placeholder array

import numpy as np


def main():
    a = np.zeros((3, 4))

    print(a)

    b = np.ones((2, 3, 4), dtype=np.int16)

    print(b)


main()
