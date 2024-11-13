# Program for creating class method

class Machine:

    # class variable

    _count = 0

    def __init__(self, name) -> None:
        Machine._count += 1
        self._id = Machine._count
        self._name = name

    # getting _id value from getter()

    def get_id(self):
        return self._id

    def __str__(self) -> str:
        return self._name

    # class method

    @classmethod
    def get_count(cls):
        return cls._count

    @classmethod
    def create(cls):
        return cls("Unknown")


def main():

    m1 = Machine("Car")
    m2 = Machine("Fan")
    m3 = Machine("Grinder")

    print(m1.get_id())
    print(m2.get_id())
    print(m3.get_id())
    print()
    print(Machine.get_count())

    m4 = Machine.create()
    print(m4)


main()
