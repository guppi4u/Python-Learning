# program for diff update


def main():
    numbers1 = {1, 2, 3, 4, 5, 6, 7}
    numbers2 = {8, 0, 3, 10, 3, 6, 9}

    print("**********************")

    # printing diff update - Removes all element of another set from this set
    print(numbers1.difference_update(numbers2))
    print(numbers1)

    print("**********************")

    # checking for superset -this will return boolean

    print({1, 2, 3, 4, 5, 6}.issuperset({1, 2, 3}))


main()
