# Creating inheritence program

import re


class IdException(Exception):
    pass


class Machine:

    def __init__(self, name, mac_id) -> None:

        # initializing machine name

        self._name = name

        # initailzing machine id

        self._mac_id = mac_id

        # checking using regex if id contains only digits

        if re.match(r"\d", str(self._mac_id)) is None:
            raise IdException("Machine id does not contain numbers!!!")

    def __str__(self) -> str:

        return f"Machine name is {self._name} and Machine id is {self._mac_id}"

    # getter method

    def get_name(self):
        return self._name

    # setter method

    def set_id(self, mac_id):
        self._mac_id = mac_id


# creating class car which inhertis method for Machine

class Car(Machine):
    pass


def main():
    car1 = Car("Maruthi", 1234)

    print(car1)

    print(f"Car name is :{car1.get_name()}")


main()
