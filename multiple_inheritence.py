class employee:
    def __init__(self,name):
        self.name=name
    def showname(self):
        print(f"the name of the employee is: {self.name}")
class player:
    def __init__(self,game):
        self.game=game
    def showgamename(self):
        print(f"the game the employee plays is: {self.game}")
    
class person(employee,player):
    def __init__(self,name,game):
        self.name=name
        self.game=game
        
pr1=person("Rupam","Badminton")
pr1.showgamename()
