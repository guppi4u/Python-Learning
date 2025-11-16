"""
Class with privte property

"""

class Person:
    def __init__(self,name,age):
        self.name =name
        self.__age =age

    def get_age(self):  # method to access private var
        return self.__age


if __name__ =="__main__":
    p1=Person("Test",20)

    print(p1.name)
    print(p1.get_age())