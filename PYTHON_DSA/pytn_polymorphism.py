"""
Prgm to demo polymorphism 
"""

class Boat:
    def __init__(self, brand,year):
        self.brand =brand
        self.year = year

    def move(self):
        print('Boat is sailing')

class Car:
    def __init__(self, brand,year):
        self.brand =brand
        self.year = year

    def move(self):
        print('Car is moving')


class Plane:
    def __init__(self, brand,year):
        self.brand =brand
        self.year = year

    def move(self):
        print('Plane is flying')


if __name__ == "__main__":
    b1 =Boat("Titanic",1912)
    c1 = Car("Tesla",2020)
    p1 =Plane("Boeing",1945)

    p1.move()
    c1.move()
    b1.move()
        