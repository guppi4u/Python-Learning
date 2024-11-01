# Python object propertises


class Dog:
    def __init__(self, name, color) -> None:
        self._name = name
        self._color = color

    def introduce(self):
        print(f"Hello, my name is {
              self._name} and my color is {self._color}")


def main():
    dog1 = Dog("Tommy", "black")
    dog2 = Dog("Goffy", "white")

    dog2.introduce()
    dog1.introduce()


main()
