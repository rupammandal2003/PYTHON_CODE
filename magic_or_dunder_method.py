class employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for character in self.name:
            i+=1
        return i
    def __str__(self):
        return f"The mname of the employee is: {self.name} --> str"
    def __repr__(self):
        return f"The mname of the employee is: {self.name} --> repr"
    def __call__(self):
        print("hey, you are a good boy")

e1=employee("Rupam")
print(e1)    
print(len(e1)) 
print(str(e1))   
print(repr(e1))   
e1()
           