class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def from_str(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e1=Employee("Rupam",12000)
print(e1.name)
print(e1.salary)

str="Rahul-15000"
e2=Employee.from_str(str)
print(e2.name)
print(e2.salary)