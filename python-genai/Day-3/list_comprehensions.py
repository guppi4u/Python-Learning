# list comprehensions 

def learning_list_compre():

    # tradational way 

    # Traditional way
    squares_tradtional = []
    for x in range(10):
        squares_tradtional.append(x ** 2)
    print(f'Squares in traditonal way : {squares_tradtional}')
    
    list_compre_squares =[x**2 for x in range(20)]

    print(f'Squares in list comprension way : {list_compre_squares}')

def filter_transform():
    # Filter and transform
    evens = [x for x in range(20) if x % 2 == 0]  
    return print(evens)

def creating_pairs():
    # Create pairs
    pairs = [(x, y) for x in range(3) for y in range(3)]
    return print(f'Paired list :{pairs}')
def multiple_conditions():
    # Multiple conditions
    filtered = [x for x in range(20) if x % 2 == 0 and x > 10]
    return print(f'Filtered list : {filtered}')

def flatten_a_2dlist():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return print(f'Flattened list :{flat}')

def list_transformation():
    # Convert to uppercase
    words = ["hello", "world"]
    upper = [word.upper() for word in words]  # ['HELLO', 'WORLD']

    # Extract specific attributes
    students = [{"name": "Alice", "age": 20}, {"name": "Bob", "age": 19}]
    names = [s["name"] for s in students]  # ['Alice', 'Bob'] 

    return print(f'Upper case list :{upper}, Dictionay key {names}')
    

    

learning_list_compre()
print()
filter_transform()
print()
creating_pairs()
print()
multiple_conditions()
print()
flatten_a_2dlist()
print()
list_transformation()