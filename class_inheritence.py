class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show_details(self):
        print(f"The name of {self.id} is {self.name}")
class addition(employee):
    def __init__(self,language):
        self.language=language
    def print_language(self):
        print(f"The programming language of the coder is {self.language}")
    def birth_country(self):
        print("The coder is from India")

a=addition("python")
a.print_language()
a.birth_country()
    