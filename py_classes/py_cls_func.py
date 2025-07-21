
class Employee:
    
    # class initializer
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    # str method similar to toString() in Java 

    def __str__(self):
        return f"{self.name},{self.age}"

    # user define method 

    def greetings(self):
        print(f'Welcome to python ,{self.name}')


emp_obj =Employee("John",22)
print(emp_obj)
print(emp_obj.greetings())