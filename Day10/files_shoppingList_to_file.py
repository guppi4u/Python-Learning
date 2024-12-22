# writing shopping list to file and reading it

# defining a shopping list

shopping_list = [
    "Milk",
    "Eggs",
    "Bread",
    "Butter",
    "Apples",
    "Chicken",
    "Rice",
    "Pasta",
    "Tomatoes",
    "Cheese"
]


def writing_file():
    with open('Day10/shopList.txt', 'w') as file:
        for item in shopping_list:
            file.write(item + '\n')


def reading_file():
    with open('Day10/shopList.txt', 'r') as file:

        # reading lines
        read_lines = file.readlines()

        # removing new line characters

        read_list = [item.strip() for item in read_lines]

        print(f'Shopping list : {read_list}')


def main():
    writing_file()
    reading_file()


main()
