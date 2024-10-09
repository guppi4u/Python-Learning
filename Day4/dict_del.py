# Program to delete dict


def main():

    fruits = {"apple": "Red",
              "banana": "Yellow",
              "cheeko": "Brown",
              "kiwi": "Green"}

    print(fruits)
    print(type(fruits))

    print("*********************************************")

    # removing items from fruits dict using "del" keword

    del fruits["apple"]

    print(fruits)
    print("*********************************************")
    # using pop

    color = fruits.pop("banana")
    print(color)
    print(fruits)


main()
