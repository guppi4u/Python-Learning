# program assiging values to tuples


def main():
    elements = (True, 3.7, 8, "goat")

    # assigning values to elements tuple
    (is_raining, weight, height, animal) = elements

    print(is_raining)
    print(weight)
    print(height)
    print(animal)

    print("*******************************************************")

    fruits = ("Apple", "Mango", "Banana", "Cherry", "Grapes")

    (fruit1, fruit2, *more_fruits, fruit4) = fruits

    print(fruit1)
    print(fruit2)
    print(more_fruits)
    print(fruit4)


main()
