
# creating add book function which takes dic of books , category and title as parameters

library = {"Fiction": {"Age Of Empires", "London daires "},
           "Cooking": {"How to cook", "How to eat"}, }


def add_book(books, category, title):

    # checking if category alredy present or not in dic

    if not category in books:
        # setting to empty set
        books[category] = set()
    # Add title to book
    books[category].add(title)


print("********************************")
# printing all the categories in the dic of books


def print_books():
    for category in library.items():
        print(category)


print("********************************")


# finding books

def find_books(library, book):
    for books in library.values():
        if book in books:
            return True

    return False


print_books()
add_book(library, "Drawing", "how to draw")
print(library)
print(find_books(library, "how to draw"))
