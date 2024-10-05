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
    show_menu()
    show_database(db)
    # add_item(db)
    # show_database(db)
    # change_item(db)
    del_item(db)
    show_database(db)


main()
