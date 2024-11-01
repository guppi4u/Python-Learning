# self in python


class Person():

    # contructor
    def __init__(self, name) -> None:
        self._name = name
        print(f"{name} created!")
        print(id(self))

    # creating a eat function
    def eat(self):
        print("I am eating")

    # creating a talk function
    def talk(self):
        print("I am talking")


def main():
    # creating person1 ,person2 variables and assigining to class

    person1 = Person("Ram")
    person2 = Person("Sam")
    person3 = Person("Jack")

    # person object calling methods from class Person
    person1.eat()
    print()
    person2.talk()
    print()
    person3.eat()
    print()

    person3.age = 60
    person2.age = 50

    print()

    print(person1._name)
    print(person2.age)
    print(person3.age)


main()
