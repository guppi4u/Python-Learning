# superconstructor


class Machine:

    # this is machine constructor
    def __init__(self, name, id) -> None:
        self._name = name
        self._id = id


# class Car inherting Machine
class Car(Machine):
    def __init__(self, name, id, type) -> None:
        # initializing name and id from machine with super() contructor
        super().__init__(name, id)
        self._type = type

    def __str__(self) -> str:
        return f"I am car of Name :{self._name}, and of type {self._type} with id {self._id}"


def main():
    car1 = Car("Tata", 1234, "SUV")

    print(car1)


main()
