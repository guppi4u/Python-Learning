# removing items from the set


def main():
    numbers = {x for x in range(20)}
    print(numbers)

    print("******************************************")

    # removing item from list
    numbers.remove(6)
    print(numbers)

    print("******************************************")

    # if we try to remove item which is not present in set, remove() will throw error

    numbers.remove(63)
    print(numbers)

    print("******************************************")

    # if we try to remove item which is not present in set, discard will  not throw error

    numbers.discard(101)
    print(numbers)
    print("no error from discard()")

    print("******************************************")


main()
