class math:
    def first_num(self,num):
        self.num=num
    def add_to_num(self,n):
        self.a=self.num+n
        print(self.a)
    @staticmethod
    def add(a,b):  # by using 'static method' no need to use self inside the function of a class
        print(a+b)
number=math()
number.first_num(5)
number.add_to_num(6)  

math.add(5,8)
number.add(58,59)    # static function can be called using both the name of the class as well as an instance ( here number is an instance of the class math) of the class 