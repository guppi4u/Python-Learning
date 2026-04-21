'''
1. Creating Dictionaries: Quickly turn two lists into key-value pairs using dict(zip(keys, values)).
2. Transposing Matrices: You can swap rows and columns of a 2D list using zip(*matrix).
3. Element-wise Calculations: Compare or perform math on items at the same position in different
 lists using zip(list1, list2).
'''

def create_dictionary_using_zip(keys, values):
    return dict(zip(keys, values))

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

name_age_dict = create_dictionary_using_zip(names, ages)
print(f'Name-Age Dictionary: {name_age_dict}')

print("*" * 30)

# Combine the lists
zipped = zip(names, ages)
print(f'Zipped Pairs: {list(zipped)}')
print("*" * 30)