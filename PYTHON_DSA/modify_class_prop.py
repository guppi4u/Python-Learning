
# creating a class with Class and modifying its class proerties

class Person:
    species = " "  # Class propertry as empty string

    def __init__(self, name):
        self.name = name  # Instance property


if __name__ == "__main__":
    p1 = Person("Ramu")
    p1.species = "New_human_name"  # modifying class property

    print(f'Person name is : {p1.name}')  # Printing instance property

    print(f'Printing class property name is : {p1.species}')
