# program on how to slice tuple

def main():
    animals = ("Cat", "Dog", "Goat", "Sheep", "Buffalo", "Hen", "Peacock")

    # Prints element at index 1
    print(animals[1])

    print("*********************")

    # Print element from 1 to 2 , 3-not included
    print(animals[1:3])

    print("*********************")

    # Print element from 2 to 5 , 6-not included
    print(animals[2:6])
    print("*********************")

    # Printing negative elements

    print(animals[-1])

    print("*********************")

    print(animals[-3:-1])


main()
