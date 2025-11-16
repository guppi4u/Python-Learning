"""
Class with privte property

"""

class Person:
    def __init__(self,name,age):
        self.name =name
        self.__age =age

    def get_age(self):  # method to access private var
        return self.__age
    

    def set_age(self,age):
        if age >0:
            self.__age =age

        else:
            print('Age must be positive')


if __name__ =="__main__":
    p1=Person("Test",20)
    p2=Person("Test2",30)
    

    print(p1.name)
    print(p1.get_age())
    
    p2.set_age(-20)