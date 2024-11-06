# Python class getters and setters


class Machine:

    def __init__(self, name, mac_id) -> None:

        # initializing machine name

        self._name = name

        # initailzing machine id

        self._mac_id = mac_id

    def __str__(self) -> str:

        return f"Machine name is {self._name} and Machine id is {self._mac_id}"

    # getter method

    def get_name(self):
        return self._name

    # setter method

    def set_id(self, mac_id):
        self._mac_id = mac_id


def main():

    # creating instance of class

    machine1 = Machine("TXH00234", 'M100')

    print(machine1)

    # getting machine name
    print(machine1.get_name())

    # setting machine id
    machine1.set_id(300)
    print(machine1)


main()
