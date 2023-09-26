# the variables which are defined inside the class that are called class variables and which are defiend inside the function of a class that are called instnce variables
# The python interpretor will search for instance variables, if any found then it will be given as output othwerwise it will take class variables
# we can change both the class and instance variables 

class company:
    company_name="Google"
    no_of_employees=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.03
        company.no_of_employees+=1
    def showDetails(self):
        print(f"The name of the employee of {self.no_of_employees} sized company {self.company_name} with raised amount {self.raise_amount} is {self.name}")

emp1=company("Rupam")
emp1.company_name="Microsoft" 
emp1.showDetails()
emp2=company("Atanu")
emp2.raise_amount=0.5
emp2.showDetails()
        
    