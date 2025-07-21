
# creating basic python Emp class 

class Employee:
    
    # class initializer
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    # string rep of class similar to toString()-in Java

    def __str__(self):
        return f" Person details :- {self.name},{self.age}"


emp_obj =Employee("John",22)

print(emp_obj)