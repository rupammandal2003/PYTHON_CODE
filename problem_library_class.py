class library:
    def no_of_books(self):
        self.no=int(input("Enter the total number of books:"))
    def books(self):
        self.a=[]
        self.c=1
        for i in range(self.no):
            self.b=input(f"Enter the {self.c} name of the book: ")
            self.a.append(self.b)
            self.c+=1
        self.d=",".join(self.a)
        print(f"your name of {self.no} books are --> {self.d}")
    def similar(self):
        if self.no==len(self.a):
            print("Yes are perfect, you have no fear to loose your job.")
        else:
            print("please recheck.")
        
l1=library()
l1.no_of_books()
l1.books()
# l1.similar()
