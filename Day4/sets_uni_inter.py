# Program for sets union , intersection , difference , symmetric_difference


def main():
    numbers1 = {1, 2, 3, 4, 5, 6, 7}
    numbers2 = {8, 0, 3, 10, 3, 6, 9}

    print("**********************")

    # printing union
    print(numbers1.union(numbers2))

    print("**********************")

    # printing intersection -this will eleminate duplicate
    print(numbers1.intersection(numbers2))

    print("**********************")

    # printing difference -Returns the diffrence of 2 or more sets as new set
    print(numbers1.difference(numbers2))

    print("**********************")

    # printing symmtric difference
    A = {'a', 'b', 'c', 'd'}
    B = {'c', 'd', 'e'}

    # returns all items to result variable except the items on intersection
    result = A.symmetric_difference(B)
    print(result)


main()
