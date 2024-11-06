

class Cow:
    def __init__(self, name, color) -> None:
        self._name = name
        self._color = color

    # creating string method

    def __str__(self) -> str:
        return f"Name :{self._name}\nWeight :{self._color}"

    def introduce(self):
        print(f"Hello, my name is {
              self._name} and my color is {self._color}")


def main():
    cow1 = Cow("Nandini", "black")
    cow2 = Cow("Bheema", "white")

    cow2.introduce()
    cow1.introduce()
    print()

    # calling string method
    print(cow1)
    print(cow2)


main()
