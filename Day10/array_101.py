# program for python array

from array import array


def main():
    numbers = array('f', [-8, 123.0, 0.0001, 87.5])

    print(numbers)

    # convertin scientific number to actual value
    print(f'{9.999999747378752e-05:f}')


main()
