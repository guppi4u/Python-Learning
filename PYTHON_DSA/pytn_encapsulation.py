"""
Class with privte property

"""

class Person:
    def __init__(self,name,age):
        self.name =name
        self.__age =age


if __name__ =="__main__":
    p1=Person("Test",20)

    print(p1.name)

    # print(p1.age) # this will trigger error 

    