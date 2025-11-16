
from pytn_inheritence import Parent
class Student(Parent):

    def __init__(self,firstname,lastname): # this is student initializer
        super().__init__(firstname,lastname) # this is parent initizlier 
        self.graduationyear=2019 # adding new attribute to student class 


    def welcomestudent(self):
        print(f'Welcome {self.firstname} {self.lastname} of graduation year {self.graduationyear}')




if __name__ =="__main__":
    
    s1=Student("Ram","Sham")
    s1.printname() # accessing parent method
    print(s1.graduationyear)

    s1.welcomestudent()



