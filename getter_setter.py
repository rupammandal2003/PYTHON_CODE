class value:
    def __init__(self,n):
        self.value=n
    def show(self):
        print(f"The value is {self.value}")
        
    @property
    def ten_value(self):
        return 10 * self.value
    @ten_value.setter
    def ten_value(self,new_value):
        self.value=new_value/10
        

a=value(10)
print(a.ten_value)
a.ten_value=521
a.show()