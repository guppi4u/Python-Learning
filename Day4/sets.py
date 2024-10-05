# Sets -- an unordered items container
# Sets only contains unique items
# represented by"{}"
# Set is mutable and faster than list and tuple
# Set can conatins multiple types of object


def main():

    numbers = {1, 1, 2, 3, 4, 5, 6}
    print(numbers)

    print("********************************")

    # converting list to set

    fruits = ["Apple", "Apple", "Mango", "Cheeko", "Banana"]

    print(set(fruits))

    print("********************************")

    # Iterating over set

    for number in numbers:
        print(number)


main()
