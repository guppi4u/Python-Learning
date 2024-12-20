# Program to use of filter function


def main():

    # this will print all the even numbers in the range of 0 and 20
    seq = filter(lambda x: x % 2 == 0, (x for x in range(0, 20)))

    print(f'This seq of even numbers between 0 and 20 is : {list(seq)}')


main()
