# Program to modify lists


def main():
    fruits = ["apple", "bananna", "cheeko", "pear"]
    print(type(fruits))
    print(fruits)

    print("********************************")

    # adding elements to list

    fruits.append("papaya")

    print(fruits)

    print("********************************")

    # this will remove all elements starting from index 2 and replaces with "kiwi"
    fruits[2:] = ["kiwi"]
    print(fruits)
    print("********************************")

    # this will remove all elements before index 2 and replaces with these
    fruits[:2] = ["lemon", "avocado", "orange"]

    print(fruits)


main()
