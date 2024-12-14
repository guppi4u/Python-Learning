# Program to discribe map()

def main():

    animals = ['CAT', 'DOG', 'GIRAFFE', 'ANT']

    # defining function lower

    def lower(str):
        return str.lower()

    # mapping function- which is iterable

    animals1 = map(lower, animals)

    # casting animals1 to list

    print(list(animals1))


main()
