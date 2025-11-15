"""
Creating class and accessing methods 
"""

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def welcome_greet(self):
        return f'Welcome to python Mr {self.name}'
    

if __name__=="__main__":
    p1 =Person("Tony",25)

    print(p1.welcome_greet()) # accessing class method