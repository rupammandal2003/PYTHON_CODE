# dir method

# a=[4,5,8,9,60]
# print(dir(a))

# __dict__ method
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

b=person("rupam",20)
print(b.__dict__)

# help() method
print(help(str))