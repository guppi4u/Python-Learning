
# Dictionary basics 

def dictionary_basics():
    books={"title":"LifeBoat",
           "author":"HarryPotter",
           "year":2000,
           "pages":500,
           "rating":4.5}
    
    print(books)
    print()
    # iterating dic in loop 
    for key,value in books.items():
        print(f'{key} : {value}')

    print()
    # updating book title 
    books['title']='DragonBird'
    print(f'Updated dictionary : {books}')
    print()
    # if "publisher" key exists, if not add it
    if "publisher" not in books:
        books['publisher'] ='penguin'

    print(f'Updated dic with publisher : {books}')
    print()
    # removing "year" key
    books.pop('year')

    print(f'Updated dicitonary with year removed :{books}')



dictionary_basics()