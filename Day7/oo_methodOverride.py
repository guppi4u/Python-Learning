# Program for method overriding


class Animal:

    def speak(self):
        print("I am speaking")

    def eat(self):
        print("I am eating!!!")


# Inheriting animal in class cat


class Cat(Animal):

    # creating overriding method for speak

    def speak(self):
        print(" Iam Cat and i can speak")


def main():
    cat1 = Cat()
    cat1.speak()
    cat1.eat()


main()
