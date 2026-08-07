"""
Circle class with property deocrator 

"""

class PCircle:
    def __init__(self,radius):
        self._radius = None # # Initialize private attribute
        self.radius = radius  # this act as setter for radius while obj creation

    @property
    def radius(self): # acts as getters 
        return self._radius

    @radius.setter
    def radius(self,value):
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

    @radius.deleter
    def raidus(self):
        print('Deleting radius...')
        del self._radius

if __name__ =="__main__":
    pcircle1 = PCircle(2.0)

    print(pcircle1.radius)

    pcircle1.radius = 3.0

    print('Radius afer modification',pcircle1.radius)

    

    print("****** Trying radius value validation *******")
    try:
        pcircle1.radius = -1.0
    except ValueError as e:
        print('Error : ',e)

    del pcircle1._radius
    print('Radius deleted')

    

    # print(pcircle1.radius)

    