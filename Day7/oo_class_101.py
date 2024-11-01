# Creating class in python


class Person():

    # creating a eat function
    def eat(self):
        print("I am eating")

    # creating a talk function
    def talk(self):
        print("I am talking")


def main():
    # creating person1 ,person2 variables and assigining to class

    person1 = Person()
    person2 = Person()

    # person object calling methods from class Person
    person1.eat()
    print()
    person2.talk()


main()
