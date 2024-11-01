# Creating constructor in python


class Person():

    # contructor
    def __init__(self, name) -> None:
        print(f"{name} created!")

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


main()
