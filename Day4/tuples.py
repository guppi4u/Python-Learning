# Program for tuples

def zoo():
    car_animals = ("Lion", "Tiger", "Lepord", "Fox")
    herb_animals = ("Elephant", "Horse", "Monkey", "Jiraffe")
    print(type(car_animals))
    print("Lenght of car_animals is : "+str(len(car_animals)))
    print(type(herb_animals))
    print("Lenght of harb_animals is : "+str(len(herb_animals)))

    print("**************************************************")

    for animal in car_animals:
        print(animal)

    print("**************************************************")

    for herb in herb_animals:
        print(herb)


def main():
    zoo()


main()
