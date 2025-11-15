'''
Creating class and modifying class propertied in a method 

'''

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def birthday_greetings(self):
        self.age += 1
        return f'Happy birthday {self.name} today and you turn {self.age} today.'
    
    def __str__(self):   # str rep of class obj 
        return f' Name : {self.name}, Age: {self.age}'
    
if __name__ == "__main__":
    p1 = Person('Max',21)
    p2=Person('Tony',63)

    print(p1) # this will print obj rep of class(if str() is missing , then it will print mem address)

    print(p2)



    print(p1.birthday_greetings(),end='\n')
    print(p2.birthday_greetings())