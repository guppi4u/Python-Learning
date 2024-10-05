# list exercies CRUD operations


def show_menu():
    print()
    options = ("Display db", "Add an item",
               "Delete item", "Change item", "Quit")
    for x in range(0, len(options)):
        print(str(x+1) + " : "+options[x])
    print()


def show_database(db):
    print()
    for i in range(0, len(db)):
        print(str(i) + " : " + db[i])
    print()


def add_item(db):
    item = input("Enter item to add :")
    db.append(item)
    pass


def del_item(db):
    item_number = input("Enter the number of the item to be removed :")
    db.pop(int(item_number))


def change_item(db):
    item_number = input("Enter number of the item change:")
    item = input("Enter new item:")
    db[int(item_number)] = item


def quit():
    pass


def main():
    db = ["apple", "orange", "mango"]

    to_do = True
    while to_do:
        show_menu()

        option = input("Select an option >")

        if option == "1":
            show_database(db)

        elif option == "2":
            add_item(db)

        elif option == "3":
            del_item(db)

        elif option == "4":
            change_item(db)

        elif option == "5":
            to_do = False

        else:
            print("Option not recognized")


main()
