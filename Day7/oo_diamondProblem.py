
# program to demonstrate diamond problem

class Device:

    def device_activate(self):
        print("Device activated!!")


class Camera(Device):
    def taking_photos(self):
        print("Taking photos!!!")


class Phone(Device):
    def making_calls(self):
        print("Making calls!!!")


class SmartPhone(Camera, Phone):
    pass


def main():
    # this class will inherit methods from both the classes
    smartDevice = SmartPhone()

    print(smartDevice.making_calls())
    print(smartDevice.taking_photos())

    # now to check from which class device_active() method will be called , we user mro()
    print(SmartPhone.mro())


main()
