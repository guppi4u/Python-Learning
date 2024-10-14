
def main():

    books = {"Cat1": {"book1", "book2", "book3"},
             "Cat2": {"book4", "book5", "book6"}}

    print(books)
    print(type(books))

    for x in books.items():
        if x not in books.keys():
            books.update()


main()
