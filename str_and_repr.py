class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # def __str__(self):
    #     return 'a {self.color} car'.format(self=self)
    
    def __repr__(self):
        return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)


my_car = Car('red', 3333)
print(my_car)