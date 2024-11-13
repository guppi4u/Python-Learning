# mro() in python stands for method resuolution order


class Animal:
    pass


class Cat(Animal):
    pass


class Rat(Animal):
    pass


class Dog(Animal):
    pass


class Tiger(Animal):
    pass


class Bengaltiger(Tiger):
    pass


def main():
    # this will print method resolution order for class Bengaltiger
    print(Bengaltiger.mro())


main()
