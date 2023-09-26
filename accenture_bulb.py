n=int(input("Enter the number of bulbs: "))
a=[]
for i in range(n):
    a.append(1)
for j in range(2,n+1):
    if j==2:
       for k in range(j,len(a)+1,j):
           a[k-1]=0
    elif 2<j<n:
       for k in range(j,len(a)+1,j):
            if a[k-1]==1:
                a[k-1]=0
            else:
                a[k-1]=1
    else:
        if a[n-1]==0:
            a[n-1]=1
        else:
            a[n-1]=0
        
        
print(a)       
print(f"At the end of the operation the number of burning bulb is: {a.count(1)}")
              