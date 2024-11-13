
# Program for multiple inheritence


class Camera:
    def taking_photos(self):
        print("Taking photos!!!")


class Phone:
    def making_calls(self):
        print("Making calls!!!")


class SmartPhone(Camera, Phone):
    pass


def main():
    # this class will inherit methods from both the classes
    smartDevice = SmartPhone()

    print(smartDevice.making_calls())
    print(smartDevice.taking_photos())


main()
