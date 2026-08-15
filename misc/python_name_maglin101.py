"""
Name manglin in python: The main purpose of name mangling is to prevent accidental attribute and method overriding when you use inheritance.

"""

class Example:
    def __init__(self,internal,private):
        self._internal = internal # can be accessed from outside class , but should not
        self.__private = private  # cannot be accessed outside class


example1 = Example('I can be accessed from outside the class, but should not',
                   'I cannot be accessed directly from outside the class')

example2 = Example(
    'I should not be accessed from outside the class',
    'But I can be accessed from outside the class with name mangling'
)
print(example1._Example__private) # I cannot be accessed directly from outside the class
print(example2._Example__private) # But I can be accessed from outside the class with name mangling



        