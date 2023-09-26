from math import pi
class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x * self.y
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area_circle(self):
        # print(f"the area of the circle is: {pi*(self.radius)**2}")
        return pi* super().area()

cir1=circle(5)
print(cir1.area_circle())       
        