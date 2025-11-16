"""
Creating class for inheritence 

"""

class Parent:

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname,self.lastname)


if __name__=="__main__":
    p1 =Parent("fname","lname")

    p1.printname()
        