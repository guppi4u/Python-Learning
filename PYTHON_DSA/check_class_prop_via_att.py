"""
Checking class and instance objects via property attribute
"""

class Dog:
    species ="German_seperd" # class prop-1
    paw = 4 # class prop-1

    def __init__(self, name, age):
        self.name =name
        self.age =age

   





if __name__=="__main__":

    dog1 =Dog("Tommy" ,10)
    dog2 =Dog("Rock" ,20)
        
    print(f'Dog 1 : {dog1.name},{dog1.age}')
    print(f'Dog 2 : {dog2.name},{dog2.age}')

    print("********************************")

    print(f'Class properties :{Dog.species}, {Dog.paw}')

    print("\n--- Using __dict__ for Checking ---")

    # dog1 only stores its unique attributes (name and age) in its dict

    print(f'dog1.__dict__:{dog1.__dict__}')

    # The class stores the class attributes (species and paws)

    print(f'Doc.__dic__ :{Dog.__dict__}')

    print()
    print("********************************")
    print()
    print(f'Printing Dog.__dic__ with keys() :{Dog.__dict__.keys()}') # printing only class dic keys
    print()
    print("********************************")
    print()
    print(f'Printing Dog.__dic__ with keys() inside list :{list(Dog.__dict__.keys())}') # printing only class dic keys inside list 
    
