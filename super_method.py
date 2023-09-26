class board:
    def noOfSchool(self):
        print("There are 1020 no of schools under this board.")
    
class school(board):
    def schoolcategory(self):
        print("all are good schools.")
        super().noOfSchool()

aa=board()
bb=school()
aa.noOfSchool()             
bb.schoolcategory()       


## using super() in constructor

# class employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class addition(employee):
#     def __init__(self,name,age,language):
#         super().__init__(name,age)
#         self.language=language

# a=employee("rupam",20)
# b=addition("rupam",20,"python")
# print(b.name)