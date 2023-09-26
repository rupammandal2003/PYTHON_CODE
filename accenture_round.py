sqr=lambda x:x*x
    

enter_num=int(input("Enter the number to check: "))

while enter_num!=1:
    a=str(enter_num)
    b=[]
    for i in a:
        b.append(int(i))
    c=0
    for j in b:
        c=c+sqr(j)
    enter_num=c
    

if enter_num==1:
    print("True")
else:
    print("False")