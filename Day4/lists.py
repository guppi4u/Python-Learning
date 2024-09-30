# Program for printing lists -lists are mutable


def main():

    animals = ["Cat", "Dog", "Rat", "Hen"]

    print(type(animals))

    print(len(animals))

   # iterating over lists
    for animal in animals:
        print(animal)

    print("*******************************")
    # Coverting tuple to list

    colors = ("red", "yellow", "blue", "green")
    colors = list(colors)

    print(type(colors))


main()
