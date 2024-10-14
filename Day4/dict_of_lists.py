# Creating dict of lists


def main():

    people = {"John": ["running", "reading", "sleeping"],
              "Doe": ["cooking", "washing", "cleaning"]}

    print(people)
    print(type(people))
    print("***********************")

    # accessing dict of list obj

    print(people["John"][1])
    print("***********************")

    # Iterating over dict of lists

    for name, hobbies in people.items():
        print(str(name) + ":" + str(hobbies))


main()
