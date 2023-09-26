n=int(input("Enter the number of bulbs: "))
a=[]
for i in range(n):
    a.append(1)
for i in range(1,n):
    if i<n-1:
        for j in range(i,n,i+1):
            if a[j]==1:
                a[j]=0
            else:
                a[j]=1
    else:
        if a[i]==0:
            a[i]=1
        else:
            a[i]=0
            
print(a.count(1))