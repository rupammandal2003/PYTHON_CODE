class employee:
    company="Apple"
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")
    @classmethod      # this method will change the class variables
    def change_company(cls,new_company):
        cls.company=new_company
e1=employee()
e1.name="Rupam"
e1.showDetails()
print(employee.company)
e1.change_company("google")
e1.showDetails()
print(employee.company)