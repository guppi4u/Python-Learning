# creating a oo exercise for python

# creating class Media

class Media:

    def __init__(self) -> None:
        pass


# following sub classes

class Book(Media):
    def __init__(self, title, author, price) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def Title(self):
        return f"Book title is {self.title}"

    def Author(self):
        return f"Book author is {self.author}"

    def Price(self):
        return f"Book price is {self.price}"

    def __str__(self) -> str:
        return f"Book name is {self.title}, author is {self.author} and price is {self.price}$"


class Movie(Media):
    def __init__(self, name, genre, year, rating) -> None:
        super().__init__()
        self.genre = genre
        self.year = year
        self.rating = rating
        self.name = name

    def Genre(self):
        return f"Move genre is {self.genre}"

    def Year(self):
        return f"Movie release year is {self.year}"

    def Rating(self):
        return f"Movie rating is {self.rating}"

    def Name(self):
        return f"Movie name is {self.name}"

    def __str__(self) -> str:
        return f"Movie genre is {self.name}, genre of {self.genre}, year of release {self.year} with customer rating {self.rating}"


class Podcast(Media):

    def __init__(self, celebs, language) -> None:
        super().__init__()
        self.celebs = celebs
        self.language = language

    def Celebs(self):
        return f"Podcast celeb is {self.celebs}"

    def Language(self):
        return f"Podcast language is {self.language}"


def main():

    book1 = Book("Mowgli", "Narayan", 100)
    book2 = Book("Batman", "Tom", 200)
    book3 = Book("Marvel", "Dick", 300)
    book4 = Book("DC", "Harry", 300)

    print(book1)
    print(book2)
    print(book3)
    print(book4)


# adding instance to container
    book_list = [book1, book2, book3, book4]


# prompting user to serch for book

    book_name = input("Enter book name :")

# Search for the book by name in the list and return the result
    book_found = None

    for book in book_list:
        if book.title.lower() == book_name.lower():
            book_found = book
            break

# displaying result based on search

    if book_found:
        print(f"Book name is {book_found.title}, author is {
              book_found.author} and price is {book_found.price}$")

    else:
        print(None)


main()
