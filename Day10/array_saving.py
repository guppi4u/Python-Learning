# program to save array as binary file and reading that file

from array import array


def main():

    # creating array for floating point numbers
    numbers = array('f', [-8, 123.0, 0.0001, 87.5])

    # creating length of array as constant

    NUMBER_ITEMS = len(numbers)

    # creating filename variable for binary file

    filename = "numbers.bin"

    # 'wb'- Wrtite Binary
    with open(filename, 'wb') as file:
        numbers.tofile(file)

    # optional step - to reclaim memory if array is big
    del numbers

    # 'rb'- Read Binary
    with open(filename, 'rb') as file:
        # creating array module with Typecode as floatingpoint number
        numbers = array('f')
        numbers.fromfile(file, NUMBER_ITEMS)

        print(numbers)


main()
