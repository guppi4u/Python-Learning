"""
Creating circle class for showing concept of @property 

"""


class Circle:
    def __init__(self,radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 *(self._radius**2)


circle1 =Circle(20)

print(f'Circle radius : {circle1.radius}')
print(f'Cricle area : {circle1.area}')

