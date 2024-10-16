# Creating dictionlay of sets


''' Algo for putting below data in suitable data structures

1. Books categories are unique
2. Books titles are unique
3. We want to easily determine which books are in which category
4. Order of books does not matter 
5. Check if book is present or not in category
6. Add books to category 

# sample data 

fiction : Age Of Empires, London daires 
Cooking : How to cook , How to eat 

# conditons 

1 .add books programtically 

2. dont assume category already exists 

3. code to print all books 

4. function to check if book is present in data structure , without knowing category 
'''


def main():
    # adding sample data to dictonary of sets
    books = {"Fiction": {"Age Of Empires", "London daires "},
             "Cooking": {"How to cook", "How to eat"}, }

    print(books)
    print(type(books))


main()
