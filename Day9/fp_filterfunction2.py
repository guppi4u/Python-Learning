# Program to use of filter function -Odd numbers


def main():

    # this will print all the even numbers in the range of 0 and 20
    seq = filter(lambda x: x % 2 == 1, (x for x in range(0, 30)))

    print(f'This seq of odd numbers between 0 and 30 is : {list(seq)}')


main()
