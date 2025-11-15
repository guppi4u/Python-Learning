
# creating a class with Class and Instance proerties 

class Person:
    species = "Human" # Class propertry 
    
    def __init__(self,name):
        self.name = name # Instance property 

        


if __name__ == "__main__":
    p1 =Person("Ramu")

    print(f'Person name is : {p1.name}') # Printing instance property

    print(f'Printing class property name is : {p1.species}')