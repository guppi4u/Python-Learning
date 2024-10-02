# List comprehensions

def main():
    animals1 = ["dog", "cat", "goat", "rat"]
    print(type(animals1))
    print(animals1)

    print("************************************")

    # converting animals list into uppper case

    animals2 = [animal.upper() for animal in animals1]
    print(animals2)

    print("************************************")

    # creating squares in number list

    numbers1 = [2, 4, 6, 8, 10]

    numbers2 = [x*x for x in numbers1]
    print(numbers2)


main()
