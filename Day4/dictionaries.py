# Program for dictionaries


def main():

    animals = {"cat": "pet",
               "dog": "pet",
               "horse": "domestic",
               "lion": "wild",
               True: "Welcome!"}

    print(type(animals))
    print(animals)
    print("***************************************")

    # accessing individual items in dict

    print(animals['horse'])
    print(animals[True])


main()
