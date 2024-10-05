# Sets add and update


def main():
    numbers = {1, 2, 3, "ball"}
    print(numbers)

    print("*****************************")

    # adding item on to set

    numbers.add(63)
    numbers.add("hello")

    print(numbers)

    print("*****************************")

    # updating list

    numbers2 = {10, 20, 30, 40}
    numbers.update(numbers2)

    print(numbers)

    print("*****************************")

    # updating sets with list

    numbers.update(["list1", "list2", "list3"])
    print(numbers)


main()
