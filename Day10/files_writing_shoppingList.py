def writing():
    with open("Day10/shopping_list.txt", 'w') as file:
        file.write("SHOPPING_LIST\n")
        file.write("1.Veggies\n")
        file.write("2.Fruits\n")
        file.write("3.Milk\n")
        file.write("4.Eggs\n")
        file.write("5.Bread\n")
        file.write("6.Drinks\n")

    print("Writing completed !!!")


def main():
    writing()


main()
