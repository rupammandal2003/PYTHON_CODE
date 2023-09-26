class parentclass:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def showdetails(self):
        print(f"name={self.name}")
        print(f"breed={self.breed}")
class childclass1(parentclass):
    def __init__(self,name,sound):
        parentclass.__init__(self,name,breed="labrador")
        self.sound=sound
    def showdetails(self):
        parentclass.showdetails(self)
        print(f"sound:{self.sound}")
class childclass2(childclass1):
    def __init__(self,name,colour):
        childclass1.__init__(self,name,sound="bark")
        self.colour=colour
    def showdetails(self):
        childclass1.showdetails(self)
        print(f"colour:{self.colour}")
        
an1=childclass2("tommy","golden")
an1.showdetails()      