# program for vairence and standard deviations


import numpy as np


def varience(data):
    mean = np.mean(data)
    # print(f' Mean of data is : {mean}')
    print("*****************")
    # this is using numpy
    print(np.mean(data))

    var = 0
    for value in data:
        var += (value-mean)**2

    var /= len(data)
    return var


def main():
    data1 = np.random.randn(3)

    print(data1)

    # varience using numpy
    print(np.var(data1))

    # standard deviation using numpy
    print(np.std(data1))

    print(varience(data1))


main()
