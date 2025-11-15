# creating a class with Class and adding new class proerties

class Person:
    species = "Human"  # Class propertry as empty string

    def __init__(self, name):
        self.name = name  # Instance property


if __name__ == "__main__":
    p1 = Person("Ramu")
    p1.age = 42

    print(f' New class property age is : {p1.age}')

    print(type(p1.age))

    print(f'Person name is : {p1.name}')  # Printing instance property

    print(f'Printing class property name is : {p1.species}')