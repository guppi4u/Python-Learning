# Program for inserting and extending lists

def main():
    animals = ["Dog", "Cat", "Rat", "Cow"]
    print(type(animals))
    print(animals)
    print("***************************************")

    # inserting another animal at index 1

    animals.insert(1, "Donkey")
    print(animals)
    print("***************************************")

    # Adding more animals item onto the lists

    more_animals = ["elephant", "camel"]
    animals.extend(more_animals)
    print(animals)
    print("***************************************")


main()
