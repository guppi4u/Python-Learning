
# program for matrices in numpy

import numpy as np


def main():

    m1 = np.arange(0, 4).reshape(2, 2)
    m2 = np.arange(1, 5).reshape(2, 2)

    print(m1)
    print()
    print(m2)
    print("******************")
    # adding both matrices m1+m2
    print(m1+m2)

    # multiplying

    print(m1*3)
    print("******************")
    print(m2*4)


main()
