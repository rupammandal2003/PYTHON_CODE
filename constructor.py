class people:
    def __init__(self,n,o):
        print("Hello guys")
        self.name=n
        self.occupation=o
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a=people("rupam","student")
a.info()