a=input()
x=[]
for i in a:
    x.append(i)
y=[]   
start=0
for i in range(len(a)):
    if i<len(a)-1:
        b=x.count(x[0])
        y.append(b-1)
        start+=1
        x=a[start:len(a)]
    else:
        b=x.count(x[0])
        y.append(b-1)
for i in y:
    print(i,end=" ")    