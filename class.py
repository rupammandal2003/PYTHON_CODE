class people:
    name="rupam"
    age=20
    hair_colour="black"
    def info(self):
        print(f"Age of {self.name} is {self.age}.")

a=people()
b=people()
a.name="atanu"
a.age=22
a.info()
b.info()