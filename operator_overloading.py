class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"{self.x} i + {self.y} y + {self.z} z"
    def __mul__(self,other):
        return vector(self.x*other.x, self.y*other.y, self.z*other.z)

v1=vector(5,4,3)
v2=vector(6,8,9)
v3=v1*v2
print(v3)