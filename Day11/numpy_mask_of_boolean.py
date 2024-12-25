# creating mask for boolean arrays

import numpy as np


def main():
    values = np.array([1, 2, 3, 4])
    bools = np.array([True, False, True, False])

    # this will print corresponding values for boolean True- Masking boolean values
    print(values[bools])


main()
