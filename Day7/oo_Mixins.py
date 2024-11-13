# Program for python mixins

class Alarm:

    def arm(self):
        print("Alarm on !!")

    def disarm(self):
        print("Alarm off !!!")


class Vehical:
    def __init__(self, seats) -> None:
        self.seats = seats

    def __str__(self) -> str:
        return f"This vehical has {self.seats} seating capacity"


class Car(Vehical, Alarm):
    pass


def main():

    TataNano = Car(6)

   # accessing both methods from Alaram(arm()) and Vehical(__str___) classes respectively
   # this is called mixin
    print(TataNano)
    TataNano.arm()


main()
